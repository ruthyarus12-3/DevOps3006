from PIL import Image, ImageDraw, ImageFont

print("------- 1 -------")
# a = 1 / 0

print("------- 2 -------")


def foo(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 0


print("------- 3 -------")


# Sure!


def boo(x, y):
    try:
        x = 1
    finally:
        print("finally")


print("------- 4 -------")
# All exception types can be caught by the "Except:"

print("------- 5 -------")
# The handle will be general and not specific according to each exception

print("------- 6 -------")
# IOError = input/output exception
# ZeroDivisionError = division by 0 cases

print("------- 7 -------")
f = open("/courseFile/words.txt", 'w')
f.write('Ruth')
f = open("/courseFile/words.txt", 'r')
lines = f.read()
print(lines)
f = open("/courseFile/words.txt", 'w')
f.write('רות')
f = open("/courseFile/words.txt", 'r')
print(f.readline())

print("------- 8 -------")
img = Image.new('RGB', (100, 30), color=(73, 109, 137))

fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
d = ImageDraw.Draw(img)
d.text((10, 10), "Hello world", font=fnt, fill=(255, 255, 0))

img.save('pil_text_font.png')
