# twitter-auto-tweet-python-selenium
## Tải tool

1. Mọi người click vào như ảnh để tải file .zip 

<img width="1120" alt="down" src="https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/0518c003-ec18-4555-9add-e6dfebfb8a4b">

2. File .zip đã được tải về máy

![image](https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/6bbea5f2-fc76-4ea8-8c28-01a60cdf5712)

3. Giải nén nó giúp em bằng cách click vào Extract

<img width="632" alt="image" src="https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/a040aff2-6c7c-487d-a46f-dea4c0de1816">

Hiện ra cái bảng mọi người cứ để nguyên và tiếp tục click vào Extract

<img width="593" alt="image" src="https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/8e649704-ee80-4613-ad2f-b9c0df7fece1">

4. Đây là folder của em sau khi em giải nén xong

- Trong đó có 1 file em khoanh lại là 1 file cần phải chỉnh sửa để tool có thể tự chạy được.

<img width="665" alt="image" src="https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/47e658b5-92bb-465e-bb0d-2251e1acd6e2">

## Cách sử dụng tool

### 1. Chỉnh sử file `tweet_content.txt` để điền nội dung cần tag

**_Note_**: Nội dung tweet không được quá 280 kí tự. Em có thêm một tính năng để check nội dung tweet trước khi đăng nhập, nên nếu lớn hơn 280 kí tự thì tool sẽ dừng và thông báo lỗi.

- Đầu tiên mở giúp em Notepad, trong thanh tìm kiếm của Window như ảnh bên dưới
  
<img width="314" alt="image" src="https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/831ab61e-fd71-4b04-8f37-abc98687442e">

- Mở lên nó sẽ trắng toát như vầy
  
![image](https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/3fbfe116-fb25-4bc5-ba88-7c4a99c7bd23)

- Click giúp em File -> Open. Sau đó tìm đến thư mục chứa tool, chọn giúp em file `tweet_content.txt`
  
<img width="814" alt="image" src="https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/8e2f5346-5898-4d62-8567-749147987dd7">

- Nội dung file sẽ hiện lên

![image](https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/cb367442-9ecf-4d9b-8429-7591b0bc93fe)

- Anh/chị có thể sửa lại nội dung file này, nó sẽ lấy nội dung trong đây để Tweet

`Auto tweet number %number%
I am a Vietnamese fan. This is the bot I use to auto tweet trending topics for the "Blank The Series"
#FayeYoko #FayePeraya #YokoApasra #BlankTheSeries |
#THHeadlineXBLANKTheSeriesSS2 #BlankTheSeriesSS2 |
`


