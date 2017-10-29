import zipfile
import string

print("* == required, [] == example, () == default_value")

file_name = input("* file name? ")
chars = input("* include chars?[1Aa]")
length = input("* length range?[1-4]")
start_at = (input("  start at?(0) ") or "0")

if not zipfile.is_zipfile(file_name):
    print("Invalid zip file")
    exit()

file_obj = zipfile.ZipFile(file_name)

log = open("log", "w")

pw = start_at

pw_dict = ""

if not chars.find("1") == -1:
    pw_dict += string.digits

if not chars.find("A") == -1:
    pw_dict += string.ascii_uppercase

if not chars.find("a") == -1:
    pw_dict += string.ascii_lowercase


def try_pw(zip_file_object, pw):
    zip_file_object.read(zip_file_object.getinfo(zip_file_object.namelist()[0]), bytes("123456", "ascii"))


def pw_go_next():
    global pw, pw_dict

    def carry_over(index):
        global pw, pw_dict
        if pw[index] == pw_dict[-1]:
            if not index <= 0:
                carry_over(index - 1)
            else:
                pw = pw_dict[0] * (len(pw) + 1)
                return pw
            pw = list(pw)
            pw[index] = pw_dict[0]
            pw = "".join(pw)
        else:
            pw = list(pw)
            pw[index] = pw_dict[pw_dict.find(pw[index]) + 1]
            pw = "".join(pw)
        return pw

    carry_over(len(pw) - 1)

