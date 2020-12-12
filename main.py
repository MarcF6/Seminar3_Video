# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




import os




# Press the green button in the gutter to run the script.


if __name__ == '__main__':


    directorio = input('Introduce el directorio del video que quieres utilizar')
    output = input('Introduce SOLO el directorio donde quieres que se guarden los videos')

    os.system("ffmpeg -i "+directorio+" -c:v libx265 "+output+"/4.mp4")
    os.system("ffmpeg -i "+directorio+" -c:v libaom-av1 "+output+"/3.mp4")
    os.system("ffmpeg -i "+directorio+" -c:v libvpx-vp9 "+output+"/2.mp4")
    os.system("ffmpeg -i " +directorio+ " -c:v libvpx -b:v 1M -c:a libvorbis "+output+"/1.webm")
    os.system("ffmpeg -i /home/scav/Escritorio/1.webm -i /home/scav/Escritorio/2.mp4 -i /home/scav/Escritorio/3.mp4 "
            "-i /home/scav/Escritorio/4.mp4 -filter_complex " "\"xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0\""  
              " /home/scav/Escritorio/exemple.mp4")

    os.system("ffmpeg -i "+output+"/1.webm -i "+output+"/2.mp4 -i "+output+"/3.mp4 -i "+output+"/4.mp4 "
                "-filter_complex " "\"xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0\"" " "+output+"/exemple.mp4""");
        #Finalmente, introduce el nuevo audio dentro del video

    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
