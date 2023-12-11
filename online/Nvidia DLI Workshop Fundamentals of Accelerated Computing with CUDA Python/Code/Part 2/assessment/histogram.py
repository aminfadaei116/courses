import numba
@numba.jit(nopython=True)
def compute_bin(x, n, xmin, xmax):
    # special case to mirror NumPy behavior for last bin
    if x == xmax:
        return n - 1 # a_max always in last bin

    # SPEEDTIP: Remove the float64 casts if you don't need to exactly reproduce NumPy
    bin = np.int32(n * (np.float64(x) - np.float64(xmin)) / (np.float64(xmax) - np.float64(xmin)))

    if bin < 0 or bin >= n:
        return None
    else:
        return bin

@cuda.jit
def cuda_histogram(x, xmin, xmax, histogram_out):
    '''Increment bin counts in histogram_out, given histogram range [xmin, xmax).'''
    nbins = histogram_out.shape[0]
    bin_width = (xmax - xmin) / nbins

    start = cuda.grid(1)
    stride = cuda.gridsize(1)

    for i in range(start, x.shape[0], stride):
        # note that calling a numba.jit function from CUDA automatically
        # compiles an equivalent CUDA device function!
        bin_number = compute_bin(x[i], nbins, xmin, xmax)

        if bin_number >= 0 and bin_number < histogram_out.shape[0]:
            cuda.atomic.add(histogram_out, bin_number, 1)
            
            