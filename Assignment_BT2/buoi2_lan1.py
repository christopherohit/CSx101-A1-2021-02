'''
Thành phố đang xây dựng tuyến đường sắt trên cao phục vụ giao thông nội đô. Tuyến đường sẽ có k+1 ga đánh số từ 0 đến k. Tàu chạy suốt ngày đêm, từ ga 0 đến ga k và quay lại. Thời gian đi từ một ga tới ga kế tiếp là 1 phút, thời gian dừng ở mỗi ga là không đáng kể. Hệ thống giao thông này không những nhanh, chuẩn xác về thời gian mà còn là một phương tiện tuyệt vời để ngắm thành phố.

BHL của UIT quyết định sẽ tặng cho tất cả tham gia lớp Python online mỗi bạn một vé đi tàu miễn phí trong năm học.

Minh rất háo hức với thông báo này và quyết tâm phải giành được một vé. Phần lớn thời gian rảnh rỗi trong ngày Minh đều dùng để rèn luyện lập trình Python, còn ban đêm là thời gian của những giấc mơ đẹp. Minh thấy mình bước lên tàu ở ga số 0, ngồi cạnh cửa sổ say sưa ngắm nhìn quang cảnh thành phố từ trên cao. Thời gian trôi đi khá nhanh. Đồng hồ cho biết Minh đã ngồi trên tàu t phút và Minh quyết định xuống tàu . . .

Chuông đồng hồ vang lên, Minh tỉnh giấc, vội vàng đi đánh răng, rửa mặt, chuẩn bị đi học. Trên đường tới trường Minh vẫn nghĩ về giấc mơ đêm qua và không thể nhớ được mình đã xuống ở ga số mấy.

Hãy xác định ga mà Minh đã xuống trong giấc mơ sắp thành hiện thực của mình.

Dữ liệu: Vào từ thiết bị nhập chuẩn gồm một dòng chứa 2 số nguyên k và t (0 < k, t ≤ 109)

Kết quả: Đưa ra thiết bị xuất chuẩn một số nguyên – ga xác định được.
'''


k , t = [int(x) for x in input().split()]

if((t//k) % 2 == 0):
    print(t%k)
else:
    print(k - t % k)