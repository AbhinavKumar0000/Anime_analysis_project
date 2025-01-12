import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("*"*99)
print("                                       ANIME ANALYSIS")
print("*"*99)
print("_"*99)
print("_"*99)
print("""Do you like Anime? or are you planning to watch some anime,  well you have come to the right place. This analysis will provide you with every information about the anime which you wanna know.""")
print("_"*99)
print("_"*99) 

print("""
-||------------------------------------------------||-
 ||Before starting we would like to get to know you||
-||------------------------------------------------||-
""")
a=input("What is your name?                              ")
b=int(input("What is your age?                               "))
c=input("What is your favourite anime?                   ")
d=input("Who is your favourite anime character?          ")
e=input("Which anime will you recommend to others?       ")
                                                                
def AR1():
    print("""
-||-----------------------------------------------------||-
 ||         Anime Recommendation Questionnaire          ||
 ||                                                     ||
 ||   Instructions for filling the Questionnaire        ||
 ||    - First letter of every word should be capital   ||
 ||    - Leave space after each word                    ||   
-||-----------------------------------------------------||-
     """)
    gen=input(" 1. Which genre do you prefer ?  ")
    epi=int(input(" 2. How many episodes do you prefer ? (Give a rough estimate)  "))
    old=int(input(" 3. How old anime do you prefer ? (Enter the year of premiere)  "))
    pre=input(" 5. What do you prefer: TV , OVA , Movie ?  ")
    if gen=="Action" and epi==25 and old==1998 and pre=="TV":
         print("You should watch : Kareshi Kanojo no Jijou")
    elif gen=="Action" and epi==200 and old==2002 and pre=="TV":
         print("You should watch : Naruto")
    elif gen=="Adventure," and epi==100 and old==1996 and pre=="TV":
         print("You should watch : Rurouni Kenshin: Meiji Kenkaku Romantan")
    elif gen=="Adventure" and epi==1 and old==2004 and pre=="Movie":
         print("You should watch : Appleseed")  
    elif gen=="Comedy" and epi==3 and old==2004 and pre=="OVA":
         print("You should watch : Ou Dorobou Jing in Seventh Heaven")        
    elif gen=="Comedy" and epi==26 and old==2001 and pre=="TV":
         print("You should watch : Fruits Basket ")        
    elif gen=="Fantasy" and epi==100 and old==1986 and pre=="TV":
         print("You should watch : One Piece")        
    elif gen=="Fantasy" and epi==150 and old==2004 and pre=="TV":
         print("You should watch : Dragon Ball z")        
    elif gen==" Supernatural" and epi==300 and old==2004 and pre=="TV":
         print("You should watch : Bleach")        
    elif gen=="Supernatural" and epi==5 and old==1991 and pre=="OVA":
         print("You should watch : Abashiri Ikka")        
    elif gen=="Drama" and epi==15 and old==1989 and pre=="OVA":
         print("You should watch : Ace wo Nerae!: Final Stage")        
    elif gen=="Drama" and epi==30 and old==2012 and pre=="Movie":
         print("You should watch : Xiao Qian")        
    elif gen=="Sci-Fi" and epi==100 and old==2005 and pre=="TV":
         print("You should watch : Planetes ")        
    elif gen=="Sci-Fi" and epi==200 and old==1995 and pre=="TV":
         print("You should watch : Galaxy Angel")        
    elif gen=="Slice of Life" and epi==25 and old==2005 and pre=="TV":
         print("You should watch : Mushishi")        
    elif gen=="Slice of Life" and epi==15 and old==2004 and pre=="OVA":
         print("You should watch : Okusama wa Joshikousei ")        
    elif gen=="Romance" and epi==100 and old==2006 and pre=="TV":
         print("You should watch : Tactical Roar")        
    elif gen=="Romance" and epi==15 and old==1997 and pre=="OVA":
         print("You should watch : Sakura Tsuushin")  
    else :
         print("Choose a correct option")

def DA2():
    print("""
-||------------------------------------------------------------||-   
 ||                 Data Analysis on Anime                     ||
 ||                                                            ||
 ||    1. Genre of anime                                       ||
 ||    2. No. of episodes of an anime                          ||
 ||    3. Anime from old to new                                ||
 ||    4. Popularity of anime                                  ||
 ||    5. Age rating of each anime                             ||
 ||    6. No. of people who are currently watching an anime    || 
 ||    7. No. of people who have completed an anime            ||
 ||    8. No. of people who have kept the anime on hold        ||
 ||    9. No. of people who planned to watch an anime          ||
 ||   10. No. of people who Dropped an anime                   ||
 ||   11. Which is more seen: TV,OVA,Movie                     ||
 ||   12. Producers of anime                                   ||
 ||   13. Studios of anime                                     ||
-||------------------------------------------------------------||-  
    """) 
    ch=int(input("Enter Your Choice "))
    if ch==1:
      gn=input("Choose an genre : a.Action , b.Slice of Life , c.Comedy , d.Adventure , e.Drama , f.Sci-Fi , g.Horror , h.Romance")
      if gn=="a":
          df=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
          df2=pd.DataFrame(df.loc[:,"Genres"])
          a=(df2[df2["Genres"]=="Action"])
          print(a)
      elif gn=="b":
          df=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
          df2=pd.DataFrame(df.loc[:,"Genres"])
          b=(df2[df2["Genres"]=="Slice of Life"])
          print(b)
      elif gn=="c":
          df=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
          df2=pd.DataFrame(df.loc[:,"Genres"])
          c=(df2[df2["Genres"]=="Comedy"])
          print(c)
      elif gn=="d":
          df=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
          df2=pd.DataFrame(df.loc[:,"Genres"])
          d=(df2[df2["Genres"]=="Adventure"])
          print(d)
      elif gn=="e":
          df=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
          df2=pd.DataFrame(df.loc[:,"Genres"])
          e=(df2[df2["Genres"]=="Drama"])
          print(e)
      elif gn=="f":
          df=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
          df2=pd.DataFrame(df.loc[:,"Genres"])
          f=(df2[df2["Genres"]=="Sci-Fi"])  
          print(f)
      elif gn=="g":
          df=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
          df2=pd.DataFrame(df.loc[:,"Genres"])
          g=(df2[df2["Genres"]=="Horror"])  
          print(g) 
      elif gn=="h":
          df=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
          df2=pd.DataFrame(df.loc[:,"Genres"])
          h=(df2[df2["Genres"]=="Romance"]) 
          print(h)
      else:
          print("Choose a correct option")
    elif ch==2:
      df=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
      df1=pd.DataFrame(df.loc[:,"Episodes"])
      dftop20=df1.head(15)
      print(dftop20)
      dftop20.plot(kind='bar',color='White', linestyle="--",edgecolor="red" , hatch="o")
      plt.ylabel("No. of Episodes")
      plt.title("No. of episodes in an anime")
      plt.show()
    elif ch==3:
      df=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
      df3=pd.DataFrame(df.loc[:,"Premiered"])
      dff=df3.sort_values("Premiered")
      print(dff)
    elif ch==4:
      df=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
      df1=pd.DataFrame(df.loc[:,"Popularity"])
      dftop2=df1.tail(20)
      print(dftop2)
      dftop2.plot(kind='bar',color='purple', linestyle="--",edgecolor="black", hatch="++")
      plt.ylabel("Popularity")
      plt.title("Anime Popularity Chart")
      plt.show()
    elif ch==5:
      df=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv" , index_col="Name" )
      df1=pd.DataFrame(df.loc[:,"Rating"])
      a=(df1[df1["Rating"]=="R - 17+ (violence & profanity)"])
      print(a)
      print("="*200)
      b=(df1[df1["Rating"]=="PG-13 - Teens 13 or older"])
      print(b)
      print("="*200)
      c=(df1[df1["Rating"]=="PG - Children"])
      print(c)
      print("="*200)
      d=(df1[df1["Rating"]=="R+ - Mild Nudity"])
      print(d)
      print("="*200)
      e=(df1[df1["Rating"]=="Rx - Hentai"])
      print(e)
      print("="*200)
      f=(df1[df1["Rating"]=="G - All Ages"])
      print(f)
    elif ch==6:
      s6=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
      df0=pd.DataFrame(s6.loc[:,"Watching"])
      df5=df0.head(15)
      print(df5)
      df5.plot(kind='bar',color='black' , linestyle="--"  , edgecolor="purple" , hatch="o-" )
      plt.title("No. of people who are currently watching an anime")
      plt.show()
    elif ch==7:
      s2=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
      dfcd=pd.DataFrame(s2.loc[:,"Completed"])
      dfw=dfcd.head(15)
      print(dfw)
      dfw.plot(kind='line',color='pink' , linestyle="-." , marker="*" , linewidth=4 , markersize=15) 
      plt.title=("No. of people who have completed an anime")
      plt.show()
    elif ch==8:
      s=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
      dfc=pd.DataFrame(s.loc[:,"On-Hold"])
      dff=dfc.head(15)
      print(dff)
      dff.plot(kind='line',color='orange' , linestyle=":" , marker="D" , linewidth=4 , markersize=10)
      plt.title("No. of people who have kept an anime on hold")
      plt.show()
    elif ch==9:
      s1=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
      df2=pd.DataFrame(s1.loc[:,"Plan to Watch"])
      dfw=df2.tail(15)
      print(dfw)
      dfw.plot(kind='bar',color='green' , edgecolor="yellow" , hatch="O.")
      plt.ylabel("No. of peolple who planned to Watch")
      plt.title("Plan to watch")
      plt.show()
    elif ch==10:
      ss=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
      df3=pd.DataFrame(ss.loc[:,"Dropped"])
      dfd=df3.head(15)
      print(dfd)
      dfd.plot(kind='bar',color='blue' , edgecolor="cyan" , hatch="*")
      plt.ylabel("No. of peolple who dropped an anime")
      plt.title("Anime dropped in between")
      plt.show()
    elif ch==11:
      df=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv" , usecols=["Type"] )
      a=(df[df["Type"]=="TV"])
      print(a)
      print("="*200)
      b=(df[df["Type"]=="OVA"])
      print(b)
      print("="*200)
      c=(df[df["Type"]=="Movie"])
      print(c)
    elif ch==12:
      se=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
      pdd=pd.DataFrame(se.loc[:,"Producers"])
      print(pdd)  
    elif ch==13:
      sf=pd.read_csv("C:/Users/abhin/Downloads/ANIME ANALYSIS/anime.csv"  , index_col="Name" )
      st=pd.DataFrame(sf.loc[:,"Studios"])
      print(st)  
    else :
      print("Choose a valid option")

def KM3():
    print("""
-||-----------------------------------------------------||-
 ||        Know more about anime before watching        ||
 ||                                                     ||
 ||    Instructions for filling the Questionnaire       ||
 ||    - First letter of every word should be capital   ||
 ||    - Leave space after each word                    ||
-||-----------------------------------------------------||-
    """) 
    sh=input("Enter the Anime of your choice ")
    if sh=="Naruto":
      print("Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed Fox, attacked Konohagakure, the Hidden Leaf Village, and wreaked havoc. In order to put an end to the Kyuubi's rampage, the leader of the village, the Fourth Hokage, sacrificed his life and sealed the monstrous beast inside the newborn Naruto. Now, Naruto is a hyperactive and knuckle-headed ninja still living in Konohagakure. Shunned because of the Kyuubi inside him, Naruto struggles to find his place in the village, while his burning desire to become the Hokage of Konohagakure leads him not only to some great new friends, but also some deadly foes.")
    elif sh=="One Piece":
      print("Gol D. Roger was known as the ""Pirate King"" the strongest and most infamous being to have sailed the Grand Line. The capture and execution of Roger by the World Government brought a change throughout the world. His last words before his death revealed the existence of the greatest treasure in the world, One Piece. It was this revelation that brought about the Grand Age of Pirates, men who dreamed of finding One Piece”which promises an unlimited amount of riches and fameâ€”and quite possibly the pinnacle of glory and the title of the Pirate King. Enter Monkey D. Luffy, a 17-year-old boy who defies your standard definition of a pirate. Rather than the popular persona of a wicked, hardened, toothless pirate ransacking villages for fun, Luffy's reason for being a pirate is one of pure wonder: the thought of an exciting adventure that leads him to intriguing people and ultimately, the promised treasure. Following in the footsteps of his childhood hero, Luffy and his crew travel across the Grand Line, experiencing crazy adventures, unveiling dark mysteries and battling strong enemies, all in order to reach the most coveted of all fortunesâ€”One Piece.")
    elif sh=="Trinity Blood":
      print("Following Armageddon, an apocalyptic war, mankind faces yet another menace: vampires. The continuous confrontations between the races have split the world into separate factions. The race of vampires, Methuselah, are affiliated with the New Human Empire; whereas the humans, deemed Terrans by the vampires, make up the Vatican Papal State. Furthermore, extremist groups like the Rosenkreuz Order strive to rekindle a war, despite the factions' attempts to avoid direct conflict. To combat terrorist organizations, the Vatican has implemented the AX unit. Led by Cardinal Caterina Sforza, the AX agents investigate vampire-related disturbances with hopes that the Terrans and the Methuselah will one day achieve a peaceful coexistence. Amongst the AX unit is priest Abel Nightroadâ€”a seemingly disoriented but gentle-hearted fellow, and a fierce vampire slayer on the battlefield. Joining the unit as his partner is a new agent, Sister Esther Blanchett, a brave and gentle young nun troubled with a tragic past. As the two grow closer, they begin to uncover signs of malicious schemes and dark forces working in the shadows. But the path they walk is riddled with misfortune that might just force them to confront the memories that plague their hearts.")
    elif sh=="Ayakashi":
      print("A child, Yuu Kusaka made a vow upon a shooting star that he would stand on the side of justice and defend the weak. However, the death of one of his friends robs him of the desire to live up to that vow, and he turns a blind eye to the misery of others, using the mysterious power he possesses as a means of making money instead of helping those in need. His days of living only for himself continue, until he's forced to fight for his life against another classmate with powers similar to his. He's saved by a mysterious girl named Eimu Yoake, who also has strange powers. Eimu reveals that his powers stem from a creature known as an Ayakashi , a parasitic being that grants the user special abilities at the price of slowly draining the life of the host. She helps him fully awaken his own. Now aware of the ayakashi he possesses, Yuu must live up to his childhood vow, putting his ayakashi to use and fend off those who would use their own for evil, all while unraveling the mystery behind the death of his friend.")
    elif sh=="Blue Period":
      print("Second-year high school student Yatora Yaguchi is bored with his normal life. He studies well and plays around with his friends, but in truth, he does not enjoy either of those activities. Bound by norms, he secretly envies those who do things differently. That is until he discovers the joy of drawing. When he sees a painting made by a member of the Art Club, Yatora becomes fascinated with the colors used in it. Later, in an art exercise, he tries to convey his language without words but instead through painting. After that experience, Yatora finds himself so invested in art that he decides that it is what he wants to do for a living. But there stand multiple obstacles in his way: his parents who are hesitant over his unique choices, his more experienced peers, and the study of a subject much deeper than he initially expected.")
    elif sh=="Wind":
      print("Beginning with a photograph of a pinhole camera by photographer Yoshiyasu Suzuka, a detailed abstract animation develops in a jet-black space.")
    elif sh=="Miracle":
      print("Music video directed by Kousuke Sugimoto for the song BEAM! by INSHOW-HA in their second mini-album ""(not) NUCLEAR LOVE (or affection)"". It features a blend of live action and animation.")
    elif sh=="Beam!":
      print("Music video by Kouki Tange and YELLOW BRAIN for the song Aishiteru by Monkey Majik in their three-song album under the same name. It features a blend of live-action and animation.")
    elif sh=="Aishiteru":
      print("Educational film meant to teach morals, to elementary through high school children.")
    elif sh=="Tejina Shi":
      print("Everyone is brand new (shinmai) at the beginning of their job. The story follows new rice (shinmai) grains in their jobs.")
    elif sh=="Shinmai":
      print("Based on a children's book of the same name. The film teaches the importance of mind and that everything is connected.")
    elif sh=="Fushou Shita Senro to Tsuki":
      print("Adaptation of Takashi Noguchi's manga, which itself adapts Baku Yumemakura's supernatural romance novel. The original novel is about a 12th-century man named Minamoto no Yoshitsune (Kurou). Kurou flees into the mountains after losing to his brother Minamoto no Yoritomo, the first Shogun to rule all of Japan. History records that he committed suicide, but instead, Kurou meets a strange, beautiful woman named Kuromitsu in her mountain hermitage. Eventually, Kurou falls in love with Kuromitsu, but then realizes she conceals a dark secret. He learns that he is unable to die and continues to live for a thousand years as Japan evolves into a future society")
    elif sh=="Kurozuka":
      print("Yorito Morimiya is obsessed with the sky. He especially loves taking pictures of its array of different facesâ€”sunrises, sunsets, clouds. On one of his early-morning excursions to photograph the sunrise, Yorito meets a strange girl engaged in an argument with a vending machine. By the time that Yorito forces the girl's tomato juice out of the machine, she's vanished without a trace. Sola follows the story of Yorito, his sister Aono, and their childhood friends Mana and Koyori Ishizuki, as well as that of a mysterious girl who appears and disappears, and who seems to harbor a dark secret. In a world where magic and the supernatural are never far below the surface and no one is who they seem to be, love and loneliness vie for supremacy beneath Yorito's sky.")
    elif sh=="Sola":
      print("This is a short, privately produced animated film. While elucidating the mystery and fuzziness as well as merits and demerits of memory in idealizing reality, the story develops into a tale of destruction of human beings, turning the existence of the earth into a memory of the universe. The production, only 5 minutes long, greatly helps expand the viewer's imagination, embodying the enchantment of animation.")
    elif sh=="Memory":
      print("While sleeping one night, Ryo Utsugi had a nightmare of monsters attacking him. One day he learns a mysterious power to let him hear voices and have visions of girls getting killed, but one night he hears the same voice.")
    elif sh=="Maou Dante":
      print("Venus Versus Virus follows regular schoolgirl Sumire who's had the ability to see ghosts since a young age. She tells friends and family about this fact and they just dismiss it, thinking she's a liar. A chance encounter with a broach flying out of nowhere, a monster and gothloli clad monster killer named Lucia leaves her with a life changing decision to use her ability and fight against these ""viruses"" feeding upon the human race.")
    elif sh=="Venus Versus Virus":
      print("Ster is a ""coyote"" or space faring outlaw who has been sitting in prison for a year for a traffic offense. Ten days from release, he breaks out with the help of his old partners Bishop and Katana. He then seeks out Franka who has been left in his care by her dead father and takes her on a journey to find her father's treasure. On their heels are the federal investigators Angelica and Chelsea as well as the android assassins of the Criminal Guild, Madame Marciano's Twelve Sisters.")
    elif sh=="Coyote Ragtime Show":
      print("To the unsuspecting eye Maki, Reimi and Yuka may not look like ace crime fighters, which might explain why they're stuck on traffic patrol instead of more" "exciting"" police duties. All that changes when Yuka gets herself kidnapped by a white slave organization run by a politically connected businessman who's got the rest of the police cowed. Now it's up to Maki and Reimi to don skin-tight battle armor, liberate a tank, and make sure that a certain slaver learns that when you play with fire, you're going to get your ass burned! ")
    elif sh=="Burn Up!":
      print("There exist creatures of darkness and evil that plague the night, devouring any human unfortunate enough to be caught in their grasp. On the other side is Hellsing, an organization dedicated to destroying these supernatural forces that threaten the very existence of humanity. At its head is Integra Fairbrook Wingates Hellsing, who commands a powerful military and spends her life fighting the undead. Integra's vast army, however, pales in comparison with her ultimate weapon: the vampire Alucard, who works against his own kind as an exterminator for Hellsing. With his new vampire servant, Seras Victoria, at his side, Alucard must battle not only monsters, but all those who stand to oppose Hellsing, be they in the guise of good or evil. In a battle for mankind's survival, Hellsing Ultimate proves that appearances are not all they may seem, and sometimes the greatest weapon can come in the form of one's worst nightmare.")
    elif sh=="Hellsing Ultimate":
      print("The Strahl candidates are enjoying a brief holiday in their various homes. However, many surprises await them when they finally come back to their elite boarding school: Rosenstolz Academy. There is a new headmaster, and his policies are not necessarily to the advantage of the main characters.")
    else:
      print("Choose a correct option")

while True:
  print("""  
-||--------------------------------------------||-
 ||                MENU TABLE                  ||
 ||  1. Anime Recommendation  Questionnaire    ||
 ||  2. Data Analysis on Anime                 ||
 ||  3. Know more about anime before watching  ||
 ||  4. Exit                                   ||   
-||--------------------------------------------||-
  """)
  ch=int(input("Enter Your Choice "))
  if ch==1:
    AR1()
  elif ch==2:
    DA2()  
  elif ch==3:
    KM3()
  elif ch==4:
    print("*"*99)
    print("                                  Thanks for visiting")
    print("*"*99)
    print("Sincere Efforts By Aastha")
    break
  else:
    print("Choose a correct option")



