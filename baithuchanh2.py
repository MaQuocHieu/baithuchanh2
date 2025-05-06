import requests

# Thông tin cần thiết
access_token = 'EAAqZBV7L3iLMBO01FapwoAxSZAqD1RXGQIaXm2afSLsTKFzAu0jhZBDx69wMQjMPHlUBc8U5b3NHFSUyS5vofTNmuo1EiLBN0bgSulGzKaNR2HTsTxHOVxd4DJoFYUsZB4ySbst46ve0r0t1wcd10mVDaNbTGaSFOifeXavPRfItQo4NMp8dyqzcUtj4e7pXXUwr7VNWVytgVfy6VAzicuP5'  # Thay bằng access token của bạn
page_id = '655557894302354'            # Thay bằng ID của trang bạn quản lý
message = 'Đây là bài viết tự động từ Python của Hiếu 🚀'  # Nội dung bài đăng

# URL API của Facebook để đăng bài
url = f'https://graph.facebook.com/{page_id}/feed'

# Dữ liệu gửi đi
payload = {
    'message': message,
    'access_token': access_token
}

# Gửi yêu cầu POST đến Facebook Graph API
response = requests.post(url, data=payload)

# Xử lý kết quả
if response.status_code == 200:
    print("✅ Đăng bài thành công!")
    print("ID bài viết:", response.json().get('id'))
else:
    print("❌ Lỗi khi đăng bài:")
    print(response.status_code)
    print(response.text)