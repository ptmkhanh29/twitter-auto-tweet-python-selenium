# twitter-auto-tweet-python-selenium
## Tải tool

Mọi người click vào link này ạ [Tool](https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium)

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

- Đầu tiên mở giúp em Notepad, trong thanh tìm kiếm của Window gõ Notepad như ảnh bên dưới
  
<img width="314" alt="image" src="https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/831ab61e-fd71-4b04-8f37-abc98687442e">

- Mở lên nó sẽ trắng toát như vầy
  
![image](https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/3fbfe116-fb25-4bc5-ba88-7c4a99c7bd23)

- Click giúp em File -> Open. Sau đó tìm đến thư mục chứa tool, chọn giúp em file `tweet_content.txt`
  
<img width="814" alt="image" src="https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/8e2f5346-5898-4d62-8567-749147987dd7">

- Nội dung file sẽ hiện lên

![image](https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/cb367442-9ecf-4d9b-8429-7591b0bc93fe)

- Anh/chị có thể sửa lại nội dung file này, nó sẽ lấy nội dung trong đây để Tweet

```python
Auto tweet number %number%

I am a Vietnamese fan. This is the bot I use to auto tweet trending topics for the "Blank The Series"

#FayeYoko #FayePeraya #YokoApasra #BlankTheSeries |

#THHeadlineXBLANKTheSeriesSS2 #BlankTheSeriesSS2 |
```

Trong file này lưu ý giúp em 2 chỗ

**1. Không xóa ` %number%` vì code nó sẽ tìm chuỗi kí tự này để thay bằng số tweet đang tự trend**

Em ví dụ: nó đã thay được `%number%` thành 334

<img width="448" alt="image" src="https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/d76a3c79-2f61-4b28-8944-4053aa24c202">

**2. Anh/chị lưu ý là ở cuối mỗi dòng tag, điền giúp em 1 kí tự nào đó vào để trắng nó tự động tìm tag => dẫn đến tag cuối sẽ bị sai.**

Em ví dụ:

Lúc đầu em trend em không có điền kí tự | sau 2 dòng tag

`#FayeYoko #FayePeraya #YokoApasra #BlankTheSeries`

và 

`#THHeadlineXBLANKTheSeriesSS2 #BlankTheSeriesSS2`

làm cho cái tag cuối nó tự nhảy qua tag khác luôn

<img width="461" alt="image" src="https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/bbcfc871-def8-4dc5-b1c4-cfefc8727753">

Nên mọi người cần điền kí tự vào, gì cũng được ạ, như em thì điền `|`

### 2. Chạy tool

Sau khi điền file xong mọi người kích đúp giúp em file `main.bat`

<img width="677" alt="image" src="https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/11e1fc8b-ac54-4da2-b49e-ae53c18c9e3c">

Nó sẽ hiện ra một giao diện như sau

![image](https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/698444dd-fd24-4fbe-8111-3cb687cf6225)

Mọi người chỉ cần lưu ý 6 chỗ em tô màu xanh là để điền là được ạ, không cần điền 2 cột màu đỏ đánh X

<img width="857" alt="image" src="https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/33a8c61a-6a99-46b4-ba8e-7cff4ece8944">

**User name**: điền user name

**Pass word**: điền password

**Start**: *đọc hướng dẫn bên dưới

**End**: *đọc hướng dẫn bên dưới

**Status**: điền `Free` (điền đúng giúp em chữ F viết hoa nha, ree viết thường)

**Verify Phone Number**: chỗ này điền số điện thoại, do trong quá trình code em có bị một chỗ là điền số điện thoại để xác thực, nên em thêm có ô này vào.

**_Hướng dẫn điền start và end_**: 

Em ví dụ: Hiện tại acc này của em đã tweet đến 334, vậy em sẽ cần điền **start** là 335 để tránh bị trùng nội dung tweet, vì X không cho đăng 2 bài có nội dung giống nhau. Còn **end** mọi người có thể điền bao nhiêu cũng được, nhưng lưu ý giới hạn 1 account 1 ngày chỉ đăng được 300 tweet. Nếu acc đó cả ngày chưa tweet gì, mọi người có thể lấy số **start** hiện tại cộng với 300 = 635 để điền vào. Sau đó nhấn submit

![image](https://github.com/ptmkhanh29/twitter-auto-tweet-python-selenium/assets/113729333/ae3603cf-c390-415f-a13c-db56716d52a4)

**_Note 1:_**: Quá trình đăng nhập có thể lâu, kéo dài 2 đến 3 phút, do em set thời gian cho mỗi bước là 60s.

**_Note 2:_**: Hiện tại tool đăng nhập suôn sẻ với acc đăng nhập 1 phát ăn ngay. Tức là nhập username, xong nhập pass => Nhấn login là đăng nhập thành công. 

**_Note 3:_**: Sau khi đăng nhập thành công, mọi người ráng ngồi xem nó, nếu có hiện bảng thông báo nào thì **Got it** giúp em nhé. 





