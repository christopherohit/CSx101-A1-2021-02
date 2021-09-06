'''
Cho biết biểu diễn dưới dạng số La Mã của một số bất kỳ

INPUT
Dòng đầu tiên chứa số n, đây là số lượng số cần đổi sang số La Mã (n < 5.000)

n dòng tiếp theo, mỗi dòng chứa 01 con số nguyên dương, đây là các số cần đổi sang số LA MÃ. Mỗi số giá trị không tới 4000

OUTPUT
n số La Mã, mỗi số trên một dòng

VÍ DỤ
Input	    Output
5
2018        MMXVIII
1923        MCMXXIII
9           IX
4           IV
99          XCIX	


MÔ TẢ SỐ LA MÃ
Số La Mã sử dụng 7 ký hiệu sau đây cho 7 mốc giá trị đặc biệt:

Symbol	I	V	X	L	C	D	M
Value	1	5	10	50	100	500	1,000
 

Các ký hiệu sẽ được ghép với nhau bằng phép toán cộng để tính ra giá trị. Tuy nhiên do một dãy 4 ký hiệu giống nhau liên tiếp cộng lại thường dễ lộn nên số 40 chẳng hạn thay vì viết XXXX sẽ được viết bằng nguyên tắc trừ thành XL (lấy 'L' - 'X' = 50 - 10 = 40).

Giải thích chi tiết trên wikipedia:
The original pattern for Roman numerals used the symbols I, V, and X (1, 5, and 10) as simple tally marks. Each marker for 1 (I) added a unit value up to 5 (V), and was then added to (V) to make the numbers from 6 to 9:

I, II, III, IIII, V, VI, VII, VIII, VIIII, X.

The numerals for 4 (IIII) and 9 (VIIII) proved problematic (among other things, they are easily confused with III and VIII, especially at a quick glance), and are generally replaced with IV (one less than 5) and IX (one less than 10). This feature of Roman numerals is called subtractive notation.

The numbers from 1 to 10 (including subtractive notation for 4 and 9) are expressed in Roman numerals as follows:

I, II, III, IV, V, VI, VII, VIII, IX, X.[2]

The system being basically decimal, tens and hundreds follow the same underlying pattern. This is the key to understanding Roman numerals:

Thus 10 to 100 (counting in tens, with X taking the place of I, L taking the place of V and C taking the place of X):

X, XX, XXX, XL, L, LX, LXX, LXXX, XC, C.

Note that 40 (XL) and 90 (XC) follow the same subtractive pattern as 4 and 9, avoiding the confusing XXXX.

Similarly, 100 to 1000 (counting in hundreds):

C, CC, CCC, CD, D, DC, DCC, DCCC, CM, M.

Again - 400 (CD) and 900 (CM) follow the standard subtractive pattern, avoiding CCCC.

In the absence of standard symbols for 5,000 and 10,000 the pattern breaks down at this point - in modern usage M is repeated up to three times. The Romans had several ways to indicate larger numbers, but for practical purposes Roman Numerals for numbers larger than 3,999 are seldom if ever used nowadays, and this suffices.

M, MM, MMM.

Many numbers include hundreds, units and tens. The Roman numeral system being basically decimal, each power of ten is added in descending sequence from left to right, as with Arabic numerals. For example:

39 = "Thirty nine" (XXX+IX) = XXXIX.
246 = "Two hundred and forty six" (CC+XL+VI) = CCXLVI.
421 = "Four hundred and twenty one" (CD+XX+I) = CDXXI.
As each power of ten (or "place") has its own notation there is no need for place keeping zeros, so "missing places" are ignored, as in Latin (and English) speech, thus:

160 = "One hundred and sixty" (C+LX) = CLX
207 = "Two hundred and seven" (CC+VII) = CCVII
1066 = "A thousand and sixty six" (M+LX+VI) = MLXVI.[3][4]
Roman numerals for large numbers are nowadays seen mainly in the form of year numbers (other uses are detailed later in this article), as in these examples:

1776 (M+DCC+LXX+VI) = MDCCLXXVI (the date written on the book held by the Statue of Liberty).[5]
1954 (M+CM+L+IV) = MCMLIV (as in the trailer for the movie The Last Time I Saw Paris)[6]
1990 (M+CM+XC) = MCMXC (used as the title of musical project Enigma's debut album MCMXC a.D., named after the year of its release).
2014 (MM+X+IV) = MMXIV (the year of the games of the XXII (22nd) Olympic Winter Games (in Sochi)
The current year (2019) is MMXIX.
'''