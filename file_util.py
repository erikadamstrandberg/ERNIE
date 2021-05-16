import os

def write_key(pair, file_string):
    file_w = open(file_string, "x")
    file_w.write(str(pair.p*pair.q) + "\n")
    key_type = file_string.split(".", 1)[1]
    if key_type == "public":
        file_w.write(str(pair.e) + "\n")
    elif key_type == "private":
        file_w.write(str(pair.d) + "\n")
    file_w.close()


def save_rsa_key(pair,foldername):
    public_key_name = "rsa.public"
    private_key_name = "rsa.private" 
    file_string_public = foldername + "/" + public_key_name
    file_string_private = foldername + "/" + private_key_name
    if not os.path.exists(foldername):
        os.mkdir(foldername)
    else:
        for files in os.listdir(foldername + "/"):
            os.remove(foldername + "/" + files)
    write_key(pair, file_string_public)
    write_key(pair, file_string_private)

