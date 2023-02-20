## end 2 end Speech recognition 

## dataset link 
`http://www.repository.voxforge1.org/downloads/SpeechCorpus/Trunk/Audio/Main/16kHz_16bit`

### step 0 (download and prepare data)
در ابتدا توصیه می‌شود از virtualenvionmet استفاده کنید که در زیر توضیحی در مورد آن داده شده است:
`https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/`

برای دانلود کردن داده ها توصیه می‌شود یک virtualenv با مشخصات زیر بسازید

```
python3.6.9
torch=1.4.0
torchvision=0.5.0
```
و بعد از فعالسازی آن با استفاده از pip نیازمندی ها را نصب نمایید
این فایل اپدیت شده است.
`pip install -r req.txt`

حال بعد از اینکه مطعن شدید که virtualenv شما فعال می‌باشد

می‌توانید اسکریپت زیر را اجرا کنید:

`bash download_prepare_data.sh`

پس از این مرحله داده‌‌های شما دانلود شده اند جهت انجام پیش‌پردازش و تبدیل داده‌های صوتی به spectrogramو داده‌های متنی به id مخصوص به ان، فایل زیر را اجرا کنید

```
python prepare_data.py
python load_data.py --train-manifest-list ./data_train.csv --valid-manifest-list ./data_val.csv  --test-manifest-list  ./data_test.csv

```
حال داده های train , validation و test اماده استفاده هستند هر کدام از انها یک شی از جنس `utils.data_loader.AudioDataLoader` هستند.

حال شما می توانید با استفاده از خروجی‌های داده شده کد خود را توسعه دهید.

## step 1: code implimentation

## step 2: results

