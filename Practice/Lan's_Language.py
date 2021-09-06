'''
Lan đang học ở một trường ngoại ngữ ở Tp.HCM. Lan rất yêu thích ngôn ngữ, đặc biệt là ngữ pháp. Khi  bước vào năm thứ 3, Lan quyết định tạo ra một ngôn ngữ mới dễ sử dụng nhất có thể đủ để nói chuyện với bạn bè. Ngôn ngữ mới của Lan có tên là Lan's Language và thỏa theo những ngữ pháp sau:

Có 3 loại từ trong Lan's Language: danh từ, động từ và tính từ. Mỗi từ trong Lan's Language thuộc một trong 3 loại từ đó.
Có 2 giới tính: Nam và Nữ. Mỗi từ trong Lan's Language thuộc một trong 2 giới tính đó.
Tính từ nam là những từ kết thúc với -lios và Tính từ nữ là những từ kết thúc với -liala.
Danh từ nam là những từ kết thúc với -etr và  Danh từ nữ là những từ kết thúc với -etra.
Động từ nam là những từ kết thúc với -initis và  Động từ nữ là những từ kết thúc với -inites.
Các từ trong Lan's Language luôn kết thúc bằng 1 trong các đuôi trên.
Các từ mà chỉ có mỗi đuôi như "lios", "liala", "etr"... cũng thuộc Lan's Language.
Không có dấu câu, ngữ pháp chia thì và các dạng biến đổi từ trong Lan's Language.
Một câu trong Lan's Language là một từ hợp lệ (thỏa những tính chất trong Lan's Language) hoặc là một mệnh đề hợp lệ.
Một mệnh đề hợp lệ trong Lan's language phải thỏa 2 điều kiện sau:

Những từ trong mệnh đề phải hợp lệ và được sắp xếp theo thứ tự: Tính từ + Danh từ + Động từ. Trong đó: Tính từ có thể có 1 hoặc nhiều hoặc không có nhưng phải đứng trước Danh từ. Chỉ có duy nhất một Danh từ trong câu. Động từ có thể có 1 hoặc nhiều hoặc không có nhưng phải đứng sau Danh từ.
Tất cả các từ trong mệnh đề phải cùng giới tính.
Cho một câu gồm một chuỗi các từ, nhiệm vụ của bạn là viết một chương trình kiểm tra xem câu được nhập vào có thỏa mãn những tính chất của Lan's language hay không? 

INPUT:

Dòng đầu tiên là một hoặc nhiều từ được viết thường bằng những kí tự Latin. Tổng số kí tự nhập vào không quá 
10
5
 (bao gồm cả khoảng trắng).

OUTPUT:

Nếu câu nhập vào thỏa mãn những tính chất của Lan's language, xuất YES
Ngược lại xuất NO

 

VÍ DỤ:

INPUT                                       OUTPUT

petr	                                    YES
etis atis animatis etis atis amatis	        NO
nataliala kataliala vetra feinites          YES
'''