# from instabot import *

# bot=Bot()

# bot.login(username="yoxshav",password="f997054407")
# bot.upload_photo("TF.jpg",caption="Logo")


from instabot import Bot
import os
import shutil


def clean_up(i):
    dir = "config"
    remove_me = "imgs\{}.REMOVE_ME".format(i)
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it so we can upload new image
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("imgs\{}".format(i))
        os.rename(remove_me, src)


def upload_post(i):
    bot = Bot()

    bot.login(username="az1k.uz", password="azizbek2002")
    bot.upload_photo("imgs/{}".format(i), caption="Caption for the post")


if __name__ == '__main__':
    # enter name of your image bellow
    image_name = "img.jpg"
    clean_up(image_name)
    upload_post(image_name)