import json
import cohere
from dotenv import load_dotenv
import os
from cohere.classify import Example

load_dotenv()

with open('song_lyrics.json', 'r') as f:
  data = json.load(f)
  lyrics = data['lyrics']


cohere_key = os.getenv("COHERE_KEY")
co = cohere.Client(cohere_key)

inputs = [lyrics
          ]


examples = [
  Example("""It might seem crazy what I am 'bout to say
          Sunshine, she's here, you can take a break
          I'm a hot air balloon that could go to space
          With the air, like I don't care, baby by the way
          Huh (Because I'm happy)
          Clap along if you feel like a room without a roof
          (Because I'm happy)
          Clap along if you feel like happiness is the truth
          (Because I'm happy)
          Clap along if you know what happiness is to you
          (Because I'm happy)
          Clap along if you feel like that's what you wanna do
          Here come bad news talking this and that (Yeah)
          Well give me all you got, don't hold back (Yeah)
          Well I should probably warn you I'll be just fine (Yeah)
          No offense to you don't waste your time
          Here's why
          Clap along if you feel like a room without a roof
          (Because I'm happy)
          Clap along if you feel like happiness is the truth
          (Because I'm happy)
          Clap along if you know what happiness is to you
          (Because I'm happy)
          Clap along if you feel like that's what you wanna do""", "happy"),
  Example("""Ah, yeah, ah, yeah
          I got this feelin' inside my bones
          It goes electric, wavy when I turn it on
          All through my city, all through my home
          We're flyin' up, no ceilin', when we in our zone
          I got that sunshine in my pocket
          Got that good soul in my feet
          I feel that hot blood in my body when it drops (ooh)
          I can't take my eyes up off it, movin' so phenomenally
          Room on lock, the way we rock it, so don't stop
          And under the lights when everything goes
          Nowhere to hide when I'm gettin' you close
          When we move, well, you already know
          So just imagine, just imagine, just imagine
          Nothin' I can see but you when you dance, dance, dance
          Feel a good, good creepin' up on you
          So just dance, dance, dance, come on
          All those things I shouldn't do
          But you dance, dance, dance
          And ain't nobody leavin' soon, so keep dancin'
          I can't stop the feelin'
          So just dance, dance, dance
          I can't stop the feelin'
          So just dance, dance, dance, come on""", "happy"),
  Example("""Ohhhh, yeeeh
          I used to think maybe you loved me now baby I'm sure
          And I just can't wait till the day when you knock on my door
          Now everytime I go for the mailbox, gotta hold myself down
          'Cause I just can't wait till you write me you're coming around
          I'm walking on sunshine, wooah
          I'm walking on sunshine, woooah
          I'm walking on sunshine, woooah
          And don't it feel good!
          Hey, alright now
          And dont it feel good!
          Hey yeah
          I used to think maybe you loved me, now I know that it's true
          And I don't want to spend my whole life, just waiting for you
          Now I don't want u back for the weekend
          Not back for a day, no no no
          I said baby I just want you back and I want you to stay
          Woah yeah!
          I'm walking on sunshine, wooah
          I'm walking on sunshine, woooah
          I'm walking on sunshine, woooah
          And don't it feel good!!
          Hey, alright now
          And don't it feel good!!
          Yeah, oh yeah
          And don't it feel good!!
          Walking on sunshine
          Walking on sunshine
          I feel alive, I feel the love, I feel the love that's really real
          I feel alive, I feel the love, I feel the love that's really real
          I'm on sunshine baby oh, oh yeah
          I'm on sunshine baby oh""", "happy"),
  Example("""Faster and faster, dear
            It's like we're moving backwards
            In your rear view mirror
            The road evened out by the snow
            Evened out by
            I can feel
            I know you feel it too
            A little flicker on the path
            We steer
            Of subtle flashing lights
            We'll go faster and faster
            This time, my mind
            It won't forget
            This time, my mind
            We're not there yet
            This time
            It goes faster and faster
            This time, my mind
            It won't forget
            This time, my mind
            We're not there yet
            This time
            It goes faster and faster
            Faster and faster, dear
            The road's still moving backwards
            Now it looks so clear
            The snow evened out by the road
            Evened out by
            I can still call the twists and turns
            But it feels so straight
            I hurried a little upon
            Until the end
            We'll go faster and faster
            This time, my mind
            It won't forget
            This time, my mind
            We're not there yet
            This time
            It goes faster and faster
            This time, my mind
            It won't forget
            This time, my mind
            We're not there yet
            This time
            It goes faster and faster""", "happy"),
  Example("""Ooh, I can't wait to get home
            I don't know why, but I'm feelin' low
            Happened again and I want you to know
            Having my woman there is good for my soul
            I try to be strong, well, I got demons
            So can I lean on you? I need a
            Strong heart and a soft touch
            And you're the one when I want love
            It's you and only you
            Who can be taken away
            The shit that I gon' do
            Each and everyday
            When I'm alone with you
            You make it better again, yeah
            Your arms are where I wanna remain
            Catch my eye, and she starts to say
            Hey, baby, we can dance slowly
            My darlin', I'll be all you need, you need
            I know it hasn't been your day or week, or week, or week
            So put it all on me
            Oh my darling, put your worries on me
            Can't judge me 'cause I feel the same thing
            And I'm here for whenever you need, you need, you ne-
            To put it all on me
            All on me, o-o-on me
            Hey baby, we can dance slowly
            All on me, o-o-on me
            Put your, put your, put your worries on me
            All on me, o-o-on me
            Hey baby, we can dance slowly
            And I'm here for whenever you need
            To put it all on me""", "happy"),
  Example("""Imagine me and you, I do
          I think about you day and night, it's only right
          To think about the girl you love and hold her tight
          So happy together
          If I should call you up, invest a dime
          And you say you belong to me, and ease my mind
          Imagine how the world could be, so very fine
          So happy together
          I can't see me lovin' nobody but you
          For all my life
          When you're with me, baby, the skies'll be blue
          For all my life
          Me and you, and you and me
          No matter how they toss the dice, it had to be
          The only one for me is you, and you for me
          So happy together
          I can't see me lovin' nobody but you
          For all my life
          When you're with me, baby, the skies'll be blue
          For all my life
          Me and you, and you and me
          No matter how they toss the dice, it had to be
          The only one for me is you, and you for me
          So happy together
          Ba-ba-ba-ba ba-ba-ba-ba ba-ba-ba ba-ba-ba-ba
          Ba-ba-ba-ba ba-ba-ba-ba ba-ba-ba ba-ba-ba-ba
          Me and you, and you and me
          No matter how they toss the dice, it had to be
          The only one for me is you, and you for me
          So happy together
          So happy together
          And how is the weather?
          So happy together
          We're happy together
          So happy together
          Happy together
          So happy together
          So happy together""", "happy"),
  Example("""Listen, baby
          Ain't no mountain high
          Ain't no valley low
          Ain't no river wide enough, baby
          If you need me, call me
          No matter where you are
          No matter how far (Don't worry baby)
          Just call my name
          I'll be there in a hurry
          You don't have to worry
          'Cause baby
          There ain't no mountain high enough
          Ain't no valley low enough
          Ain't no river wide enough
          To keep me from getting to you babe
          Remember the day
          I set you free
          I told you
          You could always count on me darlin'
          From that day on I made a vow
          I'll be there when you want me
          Some way, some how
          'Cause baby
          There ain't no mountain high enough
          Ain't no valley low enough
          Ain't no river wide enough
          To keep me from getting to you babe
          Ho no darlin'
          No wind, no rain
          Or winters cold can stop me baby, na na baby
          'Cause you are my goal
          If you're ever in trouble
          I'll be there on the double
          Just send for me, oh baby, ha
          My love is alive (Hoo)
          Way down in my heart
          Although we are miles apart
          If you ever need a helping hand
          I'll be there on the double
          Just as fast as I can
          Don't you know that
          There ain't no mountain high enough
          Ain't no valley low enough""", "happy"),
  Example("""Hello darkness, my old friend
          I've come to talk with you again
          Because a vision softly creeping
          Left its seeds while I was sleeping
          And the vision that was planted in my brain
          Still remains
          Within the sound of silence
          In restless dreams, I walked alone
          Narrow streets of cobblestone
          'Neath the halo of a street lamp
          I turned my collar to the cold and damp
          When my eyes were stabbed by the flash of a neon light
          That split the night
          And touched the sound of silence
          And in the naked light, I saw
          Ten thousand people, maybe more
          People talking without speaking
          People hearing without listening
          People writing songs that voices never shared
          And no one dared
          Disturb the sound of silence
          "Fools" said I, "You do not know
          Silence like a cancer grows
          Hear my words that I might teach you
          Take my arms that I might reach you"
          But my words, like silent raindrops fell
          And echoed in the wells of silence
          And the people bowed and prayed
          To the neon god they made
          And the sign flashed out its warning
          In the words that it was forming
          Then the sign said, "The words on the prophets
          are written on the subway walls
          In tenement halls"
          And whispered in the sound of silence""", "sad"),
  Example("""I'm tired of being what you want me to be
          Feeling so faithless, lost under the surface
          Don't know what you're expecting of me
          Put under the pressure of walking in your shoes
          Every step that I take is another mistake to you
          (Caught in the undertow, just caught in the undertow)
          I've become so numb
          I can't feel you there
          Become so tired
          So much more aware
          I'm becoming this
          All I want to do
          Is be more like me
          And be less like you
          Can't you see that you're smothering me
          Holding too tightly, afraid to lose control?
          'Cause everything that you thought I would be
          Has fallen apart right in front of you
          Every step that I take is another mistake to you
          (Caught in the undertow, just caught in the undertow)
          And every second I waste is more than I can take""", "sad"),
  Example("""When your day is long
          And the night, the night is yours alone
          When you're sure you've had enough
          Of this life, well hang on
          Don't let yourself go
          'Cause everybody cries
          Everybody hurts sometimes
          Sometimes everything is wrong
          Now it's time to sing along
          When your day is night alone (hold on, hold on)
          If you feel like letting go (hold on)
          If you think you've had too much
          Of this life, well hang on
          'Cause everybody hurts
          Take comfort in your friends
          Everybody hurts
          Don't throw your hand, oh no
          Don't throw your hand
          If you feel like you're alone
          No, no, no, you are not alone
          If you're on your own in this life
          The days and nights are long
          When you think you've had too much
          Of this life to hang on
          Well, everybody hurts sometimes
          Everybody cries
          Everybody hurts, sometimes
          And everybody hurts sometimes
          So hold on, hold on
          Hold on, hold on, hold on
          Hold on, hold on, hold on""", "sad"),
  Example("""I miss you, I miss you
          Hello, there
          The angel from my nightmare
          The shadow in the background of the morgue
          The unsuspecting victim
          Of darkness in the valley
          We can live like Jack and Sally if we want
          Where you can always find me
          And we'll have Halloween on Christmas
          And in the night, we'll wish this never ends
          We'll wish this never ends
          I miss you, I miss you
          I miss you, I miss you
          Where are you?
          And I'm so sorry
          I cannot sleep, I cannot dream tonight
          I need somebody and always
          This sick, strange darkness
          Comes creeping on, so haunting every time
          And as I stare, I counted
          The webs from all the spiders
          Catching things and eating their insides
          Like indecision to call you
          And hear your voice of treason
          Will you come home and stop this pain tonight?
          Stop this pain tonight
          Don't waste your time on me, you're already
          The voice inside my head (I miss you, I miss you)
          Don't waste your time on me, you're already
          The voice inside my head (I miss you, I miss you)
          Don't waste your time on me, you're already
          The voice inside my head (I miss you, I miss you)
          Don't waste your time on me, you're already
          The voice inside my head (I miss you, I miss you)
          Don't waste your time on me, you're already
          The voice inside my head (I miss you, I miss you)
          Don't waste your time on me, you're already
          The voice inside my head (I miss you, I miss you)""", "sad"),
  Example("""All around me are familiar faces
          Worn out places, worn out faces
          Bright and early for their daily races
          Going nowhere, going nowhere
          Their tears are filling up their glasses
          No expression, no expression
          Hide my head, I wanna drown my sorrow
          No tomorrow, no tomorrow
          And I find it kinda funny
          I find it kinda sad
          The dreams in which I'm dying
          Are the best I've ever had
          I find it hard to tell you
          I find it hard to take
          When people run in circles
          It's a very, very mad world, mad world
          Children waiting for the day they feel good
          Happy Birthday, Happy Birthday
          And I feel the way that every child should
          Sit and listen, sit and listen
          Went to school and I was very nervous
          No one knew me, no one knew me
          Hello teacher tell me what's my lesson
          Look right through me, look right through me
          And I find it kinda funny
          I find it kinda sad
          The dreams in which I'm dying
          Are the best I've ever had
          I find it hard to tell you
          I find it hard to take
          When people run in circles
          It's a very, very mad world, mad world
          Enlarging your world
          Mad world""", "sad"),
  Example("""I still see your shadows in my room
          Can't take back the love that I gave you
          It's to the point where I love and I hate you
          And I cannot change you so I must replace you (oh)
          Easier said than done
          I thought you were the one
          Listening to my heart instead of my head
          You found another one, but
          I am the better one
          I won't let you forget me
          I still see your shadows in my room
          Can't take back the love that I gave you
          It's to the point where I love and I hate you
          And I cannot change you so I must replace you (oh)
          Easier said than done
          I thought you were the one
          Listening to my heart instead of my head
          You found another one, but
          I am the better one
          I won't let you forget me
          You left me falling and landing inside my grave
          I know that you want me dead
          I take prescriptions to make me feel a-okay
          I know it's all in my head
          I have these lucid dreams where I can't move a thing
          Thinking of you in my bed
          You were my everything
          Thoughts of a wedding ring
          Now I'm just better off dead
          I'll do it over again
          I didn't want it to end
          I watch it blow in the wind
          I should've listened to my friends
          Did this shit in the past
          But I want it to last
          You were made outta plastic (fake)
          I was tangled up in your drastic ways
          Who knew evil girls have the prettiest face?
          You gave me a heart that was full of mistakes
          I gave you my heart and you made heart break
          """, "sad"),
  Example("""I hurt myself today
          To see if I still feel
          I focus on the pain
          The only thing that's real
          The needle tears a hole
          The old familiar sting
          Try to kill it all away
          But I remember everything
          What have I become?
          My sweetest friend
          Everyone I know goes away
          In the end
          And you could have it all
          My empire of dirt
          I will let you down
          I will make you hurt
          I wear this crown of thorns
          Upon my liar's chair
          Full of broken thoughts
          I cannot repair
          Beneath the stains of time
          The feelings disappear
          You are someone else
          I'm still right here
          What have I become?
          My sweetest friend
          Everyone I know goes away
          In the end
          And you could have it all
          My empire of dirt
          I will let you down
          I will make you hurt
          If I could start again
          A million miles away
          I would keep myself
          I would find a way""", "sad"),
  Example("""Turn down the lights
          Turn down the bed
          Turn down these voices inside my head
          Lay down with me
          Tell me no lies
          Just hold me close, don't patronize
          Don't patronize me
          'Cause I can't make you love me if you don't
          You can't make your heart feel something it won't
          Here in the dark, in these final hours
          I will lay down my heart and I'll feel the power
          But you won't, no you won't
          'Cause I can't make you love me, if you don't
          I'll close my eyes, then I won't see
          The love you don't feel when you're holding me
          Morning will come and I'll do what's right
          Just give me till then to give up this fight
          And I will give up this fight
          'Cause I can't make you love me if you don't
          You can't make your heart feel something it won't
          Here in the dark, in these final hours
          I will lay down my heart and I'll feel the power
          But you won't, no you won't
          'Cause I can't make you love me, if you don't""", "sad"),
  Example("""
  [Produced by Kanye West, Mike Dean, and Timbaland]

[Intro: Daft Punk]
Work it, make it, do it, makes us
Harder, better, faster, stronger

[Chorus: Kanye West & Daft Punk]
N-Now th-that that don't kill me
Can only make me stronger
I need you to hurry up now
'Cause I can't wait much longer
I know I got to be right now
'Cause I can't get much wronger
Man, I've been waiting all night now
That's how long I been on ya
(Work it harder, make it better
Do it faster, makes us stronger)
(I need you right now!)
(More than ever, hour after hour
Work–)
(I need you right now!)

[Verse 1: Kanye West]
Let's get lost tonight
You could be my black Kate Moss tonight
Play secretary, I'm the boss tonight
And you don't give a fuck what they all say, right?
Awesome, the Christian in Christian Dior
Damn, they don't make 'em like this anymore
I ask, 'cause I'm not sure
Do anybody make real shit anymore?
Bow in the presence of greatness
'Cause right now, thou hast forsaken us
You should be honored by my lateness
That I would even show up to this fake shit
So go ahead, go nuts, go apeshit!
'Specially in my Pastellé, on my Bape shit
Act like you can't tell who made this
New Gospel, homie, take six
And take this, haters!

[Chorus: Kanye West & Daft Punk]
N-Now th-that that don't kill me
Can only make me stronger
I need you to hurry up now
'Cause I can't wait much longer
I know I got to be right now
'Cause I can't get much wronger
Man, I've been waiting all night now
That's how long I been on ya
(Work it harder, make it better
Do it faster, makes us stronger)
(I need you right now!)
(More than ever, hour after hour
Work–)
(I need you right now!) Me likey!

[Verse 2: Kanye West & Daft Punk]
I don't know if you got a man or not
If you made plans or not
If God put me in your plans or not
I'm trippin', this drink got me saying a lot
But I know that God put you in front of me
So how the hell could you front on me?
There's a thousand you's, there's only one of me
I'm trippin', I'm caught up in the moment, right?
'Cause it's Louis Vuitton Don night
So we gon' do everything that Kan like
Heard they'd do anything for a Klondike
Well, I'd do anything for a blonde dyke
And she'll do anything for the limelight
And we'll do anything when the time's right
Uh, baby, you're makin' it–
(Harder, better, faster, stronger)

[Chorus: Kanye West & Daft Punk]
N-Now th-that that don't kill me (Oh)
Can only make me stronger (Oh)
I need you to hurry up now (Oh)
'Cause I can't wait much longer (Oh)
I know I got to be right now (Oh)
'Cause I can't get much wronger (Oh)
Man, I've been waiting all night now
That's how long I been on ya
(Work it harder, make it better
Do it faster, makes us stronger)
(I need you right now!)
(I need you right now!)

[Bridge: Kanye West & Daft Punk]
You know how long I've been on ya
Since Prince was on Apollonia
Since O.J. had Isotoners
Don't act like I never told ya
Don't act like I never told ya
Don't act like I never told ya
Don't act like I never told ya
Don't act like I never told ya
Baby, you're makin' it
(Harder, better, faster, stronger)

[Chorus: Kanye West & Daft Punk]
N-Now th-that that don't kill me
Can only make me stronger
I need you to hurry up now
'Cause I can't wait much longer
I know I got to be right now
'Cause I can't get much wronger
Man, I've been waiting all night now
That's how long I been on ya
(Work it harder, make it better
Do it faster, makes us stronger)
(I need you right now!)
(I need you right now!)
Right now!
Work it harder, make it better
Do it faster, makes us stronger
(I need you right now!)
(I need you right now!)

[Bridge: Kanye West]
You know how long I've been on ya
Since Prince was on Apollonia
Since O.J. had Isotoners
Don't act like I never told ya
You know how long I've been on ya
Since Prince was on Apollonia
Since O.J. had Isotoners
Don't act like I never told ya

[Outro]
Told ya, told ya
Never told ya …told ya, told ya, told ya
Never told ya …told ya, told ya, told ya
Never told ya …told ya, told ya, told ya
Never told ya …told ya, told ya, told ya
Never over …Never over … Never over … Never over …
Never over …Never over … Never over … Never over …
(Harder, better, faster, stronger)
Work it harder, make it better
Do it faster, makes us stronger
More than ever, hour after hour
Work is never over
Work it harder, make it better
Do it faster, makes us stronger
More than ever, hour after hour
Work is never over
Work it harder, make it better
Do it faster, makes us stronger
More than ever, hour after hour
Work is never over
Work it harder, make it better
Do it faster, makes us stronger
More than ever, hour after hour
Work is never over
  """ , "happy")
]
response = co.classify(
  model='large',
  inputs=inputs,
  examples=examples)

print(response.classifications)


