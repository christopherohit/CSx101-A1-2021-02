'''
Theo hệ 12 con giáp chúng ta có 10 can là:
GIÁP, ẤT, BÍNH, ĐINH, MẬU, KỶ, CANH, TÂN, NHÂM, QUÝ

và 12 con giáp là

TÝ, SỬU, DẦN, MẸO, THÌN, TỴ, NGỌ, MÙI, THÂN, DẬU, TUẤT, HỢI

Để đặt tên cho một năm âm lịch, người ta sẽ ghép một can với một con giáp. 
Năm tiếp theo sẽ mang tên của can tiếp theo và con giáp tiếp theo. 
Ví dụ năm 2015 là năm ẤT MÙI thì năm 2016 sẽ mang can tiếp theo là BÍNH và con giáp tiếp theo là THÂN, 
như vậy năm 2016 là năm BÍNH THÂN. Một công ty X muốn nhảy vào thị trường làm lịch, 
hãy giúp công ty X viết phần mềm tính tên âm lịch cho năm.

INPUT
Một con số nguyên khác 0 có trị tuyệt đối không quá 1 tỷ. Đây là năm cần xét, 
năm trước công nguyên được quy ước ghi bằng số âm và năm sau công nguyên quy ước ghi bằng số dương.

OUTPUT
Tên âm lịch của năm đó, viết hoa toàn bộ, không bỏ dấu. 
Quy ước để phân biệt Tý và Tỵ thì Tý sẽ viết với dấu nháy kép thay cho dấu sắc

TY'

và Tỵ sẽ viết với dấu chấm câu thay cho dấu nặng:

TY.
'''
def canchi(n):
    if n < 0:
        x = (n + 1) % 10
        y = (n + 1) % 12
    else:
        x = n % 10
        y = n % 12

    
    can={
        0:'CANH',
        1:'TAN',
        2:'NHAM',
        3:'QUY',
        4:'GIAP',
        5:'AT',
        6:'BINH',
        7:'DINH',
        8:'MAU',
        9:'KY'
    }
    chi = {
        0:'THAN',
        1:'DAU',
        2:'TUAT',
        3:'HOI',
        4:"TY'",
        5:"SUU",
        6:'DAN',
        7:'MEO',
        8:'THIN',
        9:'TY.',
        10:'NGO',
        11:'MUI',
    }
    return can.get(x,"")+ " " + chi.get(y,"")



n = int(input())
print(canchi(n))
