X = float(input())
Y = float(input())
Z = float(input())
T = float(input())

rect_w = X
if Z < rect_w:
    rect_w = Z

rect_h = Y
if T < rect_h:
    rect_h = T

rect_area = rect_w * rect_h

tri_a = X - Z
if tri_a < 0:
    tri_a = -tri_a

tri_b = Y - T
if tri_b < 0:
    tri_b = -tri_b

tri_area = 0.5 * tri_a * tri_b

print(rect_area + tri_area)
