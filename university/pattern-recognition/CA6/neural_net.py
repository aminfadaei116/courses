import numpy as np
import matplotlib.pyplot as plt

class MLPNet(object):

  """
  In this class we implement a MLP neural network. 
  H: hidden layer size
  N: input size
  D: Number of features
  C: class
  Loss Function: Softmax
  Regularization: L2 norm
  Activation Function: ReLU
  
  """
  def __init__(self, D, H, output_size, std=1e-4):
    """
    In this part we initialize the model as below:
    weights are initialize with small random value and biases are initialized with zero value. 
    these values are stored in the self.p_net as dictionary
    """
    self.p_net = {}
    self.p_net['W1'] = std * np.random.randn(D, H)
    self.p_net['b1'] = np.zeros(H)
    self.p_net['W2'] = std * np.random.randn(H, output_size)
    self.p_net['b2'] = np.zeros(output_size)

  def loss(self, X, y=None, reg=0.0):

    """
      calculate the loss and its gradients for network:
      our inputs are:
        X: N*D matrix 
        y: training labels

      Returns:
      if y is empty :
        -return score matrix with shape (N,C) .each element of this matrix shows score for class c on input X[i]
      otherwise:
        -return a tuple of loss and gradient.
    """
    Weight2, bias2 = self.p_net['W2'], self.p_net['b2']
    Weight1, bias1 = self.p_net['W1'], self.p_net['b1']
    N, D = X.shape

    # forward pass
    scores = None

    #############################################################################
    def ReLU(input_) :
      output_ = input_.copy()
      for i in output_ :
        for j in i :
          j = max(j , 0)
      return output_

    HW = ReLU(X.dot(Weight1) + bias1)
    scores = ReLU(HW.dot(Weight2) + bias2)
    #############################################################################
    
    if y is None:
      return scores

    # fill loss function.
    loss = None
    #############################################################################
    LOSS_LAMBDA = 1e-4
    
    exp_scores = np.exp(scores)
    expSums = np.sum(exp_scores,axis=1)
    
    def lossCal(i) :
      if(exp_scores[i][y[i]] == 0) : return 0
      if(expSums[i] == 0) : return 0
      return -np.log(exp_scores[i][y[i]]/expSums[i])

    sampleLoss = np.array(list(map(lambda i: lossCal(i) , range(N))))
    regularization = LOSS_LAMBDA*(np.sum(Weight1)+np.sum(Weight2))/2
    loss = np.sum(sampleLoss)/N + regularization
    #############################################################################

    # calculate gradients
    gradient = {}
    #############################################################################
    def gradientFunc(L, d, W1=Weight1, W2=Weight2, b1=bias1, b2=bias2, dw1=0, dw2=0, db1=0, db2=0) :
      return (L(W1+dw1, W2+dw2, b1+db1, b2+db2) - L(W1, W2, b1, b2)) / d

    def lossOf_(W1, W2, b1, b2) :
      this_HW = X.dot(W1) + b1
      this_Scores = this_HW.dot(W2) + b2
      this_exp_scores = np.exp(this_Scores)
      this_expSum = np.sum(this_exp_scores, axis=1)
      def lossCal(i) :
        if(this_exp_scores[i][y[i]] == 0) : return 0
        if(this_expSum[i] == 0) : return 0
        return -np.log(this_exp_scores[i][y[i]]/this_expSum[i])

      this_sampleLoss = np.array(list(map(lambda i: lossCal(i), range(N))))
      this_regularization = LOSS_LAMBDA*(np.sum(W1)+np.sum(W2))/2
      this_loss = np.sum(this_sampleLoss)/N + this_regularization
      return this_loss

    w1Grad = lambda w1 : gradientFunc(lossOf_, d, dw1=w1)
    w2Grad = lambda w2 : gradientFunc(lossOf_, d, dw2=w2)
    b1Grad = lambda b1 : gradientFunc(lossOf_, d, db1=b1)
    b2Grad = lambda b2 : gradientFunc(lossOf_, d, db2=b2)

    d = 1e-4

    def dMatrixMaker2d(shape, d) :
      matrixs = []
      baseMatrix = np.zeros(shape.shape)
      for i in range(shape.shape[0]) :
        for j in range(shape.shape[1]) :
          baseMatrix[i][j] += d
          matrixs.append(baseMatrix.copy())
          baseMatrix[i][j] -= d
      return matrixs

    def dMatrixMaker(shape, d) :
      matrixs = []
      baseMatrix = np.zeros(shape.shape)
      for i in range(shape.shape[0]) :
        baseMatrix[i] += d
        matrixs.append(baseMatrix.copy())
        baseMatrix[i] -= d
      return matrixs
      
    gradient['W1'] = np.array(list(map(w1Grad , (dMatrixMaker2d(Weight1, d))))).reshape(Weight1.shape)
    gradient['W2'] = np.array(list(map(w2Grad , (dMatrixMaker2d(Weight2, d))))).reshape(Weight2.shape)
    gradient['b1'] = np.array(list(map(b1Grad , (dMatrixMaker(bias1, d))))).reshape(bias1.shape)
    gradient['b2'] = np.array(list(map(b2Grad , (dMatrixMaker(bias2, d))))).reshape(bias2.shape)
    #############################################################################

    return loss, gradient

  def train(self, X, y, X_val, y_val,
            learning_rate=1e-3, learning_rate_decay=0.95,
            reg=1e-5, num_iters=100,
            batch_size=100):

    """
    We want to train this network with stochastic gradient descent.
    Our inputs are:

    - X: array of shape (N,D) for training data.
    - y: training labels.
    - X_val: validation data.
    - y_val: validation labels.
    - learning_rate: learning rate
    - learning_rate_decay: This factor used to decay the learning rate after each epoch
    - reg: That shows regularization .
    - num_iters: Number of epoch 
    - batch_size: Size of each batch

    """
    N = X.shape[0]

    num_train = X.shape[0]
    iteration = max(num_train / batch_size, 1)

    loss_train = []
    train_acc = []
    val_acc = []

    for it in range(num_iters):
      data_batch = None
      label_batch = None

      #########################################################################
      choosenIndexes = np.random.choice(N, batch_size)
      data_batch = X[choosenIndexes]
      label_batch = y[choosenIndexes]
      #########################################################################

      # calculate loss and gradients
      loss, gradient = self.loss(data_batch, y=label_batch, reg=reg)
      loss_train.append(loss)

      #########################################################################
      self.p_net['W1'] -= learning_rate*gradient['W1']
      self.p_net['W2'] -= learning_rate*gradient['W2']
      self.p_net['b1'] -= learning_rate*gradient['b1']
      self.p_net['b2'] -= learning_rate*gradient['b2']
      #########################################################################

      if it % 5 == 0:
        print ('iteration %d / %d: loss %f' % (it, num_iters, loss))

      if True : # it % iteration == 0:
        # Check accuracy
        acc = (self.predict(data_batch) == label_batch).mean()
        valacc = (self.predict(X_val) == y_val).mean()
        # print(acc, valacc)
        train_acc.append(acc)
        val_acc.append(valacc)

        learning_rate *= learning_rate_decay

    return {
      'loss_train': loss_train,
      'train_acc': train_acc,
      'val_acc': val_acc,
    }

  def predict(self, X):

    """
    After you train your network use its parameters to predict labels

    Returns:
    - y_prediction: array which shows predicted lables
    """
    y_prediction = None

    ###########################################################################
    y_prediction = list(map(lambda array: list(array).index(max(array)), self.loss(X)))
    ###########################################################################

    return y_prediction


