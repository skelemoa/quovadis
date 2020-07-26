# Skeletics 152

### Introduction

Skeletics 152 is a in the wild human action dataset made using the videos from much larger [Kinetics-700 dataset](https://deepmind.com/research/publications/A-Short-Note-on-the-Kinetics-700-Human-Action-Dataset)

Since Kinetics 700 contains many categories which can't be considered to be of human actions, a more focused subset of these categories was manually picked and this Skeletics 152 dataset was created.

<center>
<table >
  <tr>
    <th/>
    <th>Number of classes</th>
    <th>Number of Samples</th>
  </tr>

  <tr>
    <td>Kinetics 700</td>
    <td>700</td>
    <td>650,000</td>
  </tr>

  <tr>
    <td>Skeletics 152</td>
    <td>152</td>
    <td>125,621</td>
  </tr>
</table>
</center>

### Downalod Dataset

Skeletics 152 dataset can be downloaded from this <a href = "">link</a>

A .zip file will be downloaded from this link which will contain, two more .zip files:
1. vibe_results_train.zip
2. vibe_results_val.zip

Which contains VIBE skeleton results for train and validation split respecitvely.

Inside each of these .zip files there will be folders with the name of different classes and inside each folder there will be json files containing VIBE skeleon results for different video samples in that class.

### Dataset preparation

To obtain 3d skeletons from the RGB video, [VIBE pose estimation model](https://github.com/mkocabas/VIBE) is used. VIBE pose estimate gives 49 joints in total out of which we are choosing the first **25**
body joints common with [Openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose). The joint ordering for Openpose is [here](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/output.md#keypoint-ordering-in-cpython).
The final videos are then split randomly into 80:20 train-val split.

### Samples

Some samples of the vibe skeleton estimations on the RGB video are shown below.


<table>
<tr>
  <td>
    <img src = "../static/skeletics_1.gif"/>
  </td>
  <td>
    <img src = "../static/skeletics_2.gif" />
  </td>
  <td>
    <img src = "../static/skeletics_3.gif"/>
  </td>
</tr>

<tr>
  <td align="center">Clean And Jerk</td>
  <td align="center">Front Raise</td>
  <td align="center">Mountain</td>
</tr>

</table>


### Selected Classes

<table>

<tr>
	<td align = "center">**A1** tai chi</td>
	<td align = "center">**A2** walking with crutches</td>
	<td align = "center">**A3** juggling soccer ball</td>
</tr>
<tr>
	<td align = "center">**A4** dribbling basketball</td>
	<td align = "center">**A5** catching or throwing softball</td>
	<td align = "center">**A6** playing organ</td>
</tr>
<tr>
	<td align = "center">**A7** catching or throwing baseball</td>
	<td align = "center">**A8** taking photo</td>
	<td align = "center">**A9** robot dancing</td>
</tr>
<tr>
	<td align = "center">**A10** playing cello</td>
	<td align = "center">**A11** training dog</td>
	<td align = "center">**A12** tiptoeing</td>
</tr>
<tr>
	<td align = "center">**A13** pumping fist</td>
	<td align = "center">**A14** contact juggling</td>
	<td align = "center">**A15** skipping stone</td>
</tr>
<tr>
	<td align = "center">**A16** playing piccolo</td>
	<td align = "center">**A17** front raises</td>
	<td align = "center">**A18** dancing gangnam style</td>
</tr>
<tr>
	<td align = "center">**A19** head stand</td>
	<td align = "center">**A20** side kick</td>
	<td align = "center">**A21** push up</td>
</tr>
<tr>
	<td align = "center">**A22** riding a bike</td>
	<td align = "center">**A23** stretching arm</td>
	<td align = "center">**A24** bench pressing</td>
</tr>
<tr>
	<td align = "center">**A25** casting fishing line</td>
	<td align = "center">**A26** disc golfing</td>
	<td align = "center">**A27** playing accordion</td>
</tr>
<tr>
	<td align = "center">**A28** playing ping pong</td>
	<td align = "center">**A29** air drumming</td>
	<td align = "center">**A30** chopping wood</td>
</tr>
<tr>
	<td align = "center">**A31** country line dancing</td>
	<td align = "center">**A32** tightrope walking</td>
	<td align = "center">**A33** catching or throwing frisbee</td>
</tr>
<tr>
	<td align = "center">**A34** exercising with an exercise ball</td>
	<td align = "center">**A35** riding mechanical bull</td>
	<td align = "center">**A36** rope pushdown</td>
</tr>
<tr>
	<td align = "center">**A37** digging</td>
	<td align = "center">**A38** situp</td>
	<td align = "center">**A39** shearing sheep</td>
</tr>
<tr>
	<td align = "center">**A40** breaking boards</td>
	<td align = "center">**A41** playing guitar</td>
	<td align = "center">**A42** golf driving</td>
</tr>
<tr>
	<td align = "center">**A43** playing drums</td>
	<td align = "center">**A44** riding mule</td>
	<td align = "center">**A45** playing ukulele</td>
</tr>
<tr>
	<td align = "center">**A46** hula hooping</td>
	<td align = "center">**A47** javelin throw</td>
	<td align = "center">**A48** singing</td>
</tr>
<tr>
	<td align = "center">**A49** clapping</td>
	<td align = "center">**A50** snatch weight lifting</td>
	<td align = "center">**A51** snorkeling</td>
</tr>
<tr>
	<td align = "center">**A52** golf chipping</td>
	<td align = "center">**A53** clean and jerk</td>
	<td align = "center">**A54** sweeping floor</td>
</tr>
<tr>
	<td align = "center">**A55** passing soccer ball</td>
	<td align = "center">**A56** long jump</td>
	<td align = "center">**A57** playing harp</td>
</tr>
<tr>
	<td align = "center">**A58** tackling</td>
	<td align = "center">**A59** skiing slalom</td>
	<td align = "center">**A60** playing field hockey</td>
</tr>
<tr>
	<td align = "center">**A61** golf putting</td>
	<td align = "center">**A62** playing harmonica</td>
	<td align = "center">**A63** swinging on something</td>
</tr>
<tr>
	<td align = "center">**A64** longboarding</td>
	<td align = "center">**A65** jumping into pool</td>
	<td align = "center">**A66** snowboarding</td>
</tr>
<tr>
	<td align = "center">**A67** bowling</td>
	<td align = "center">**A68** shoot dance</td>
	<td align = "center">**A69** saluting</td>
</tr>
<tr>
	<td align = "center">**A70** deadlifting</td>
	<td align = "center">**A71** jumping jacks</td>
	<td align = "center">**A72** bouncing on bouncy castle</td>
</tr>
<tr>
	<td align = "center">**A73** playing squash or racquetball</td>
	<td align = "center">**A74** shot put</td>
	<td align = "center">**A75** yoga</td>
</tr>
<tr>
	<td align = "center">**A76** falling off chair</td>
	<td align = "center">**A77** playing tennis</td>
	<td align = "center">**A78** swinging baseball bat</td>
</tr>
<tr>
	<td align = "center">**A79** moon walking</td>
	<td align = "center">**A80** archery</td>
	<td align = "center">**A81** stretching leg</td>
</tr>
<tr>
	<td align = "center">**A82** checking watch</td>
	<td align = "center">**A83** climbing a rope</td>
	<td align = "center">**A84** pull ups</td>
</tr>
<tr>
	<td align = "center">**A85** tobogganing</td>
	<td align = "center">**A86** hitting baseball</td>
	<td align = "center">**A87** pushing cart</td>
</tr>
<tr>
	<td align = "center">**A88** paragliding</td>
	<td align = "center">**A89** running on treadmill</td>
	<td align = "center">**A90** high fiving</td>
</tr>
<tr>
	<td align = "center">**A91** cumbia</td>
	<td align = "center">**A92** battle rope training</td>
	<td align = "center">**A93** playing oboe</td>
</tr>
<tr>
	<td align = "center">**A94** sword swallowing</td>
	<td align = "center">**A95** biking through snow</td>
	<td align = "center">**A96** playing violin</td>
</tr>
<tr>
	<td align = "center">**A97** jogging</td>
	<td align = "center">**A98** opening door</td>
	<td align = "center">**A99** chiseling stone</td>
</tr>
<tr>
	<td align = "center">**A100** abseiling</td>
	<td align = "center">**A101** hammer throw</td>
	<td align = "center">**A102**  standing on hands</td>
</tr>
<tr>
	<td align = "center">**A103** sword fighting</td>
	<td align = "center">**A104** dunking basketball</td>
	<td align = "center">**A105** reading book</td>
</tr>
<tr>
	<td align = "center">**A106** jumpstyle dancing</td>
	<td align = "center">**A107** cutting cake</td>
	<td align = "center">**A108** belly dancing</td>
</tr>
<tr>
	<td align = "center">**A109** exercising arm</td>
	<td align = "center">**A110** pushing wheelbarrow</td>
	<td align = "center">**A111** pushing car</td>
</tr>
<tr>
	<td align = "center">**A112** lunge</td>
	<td align = "center">**A113** hopscotch</td>
	<td align = "center">**A114** ski ballet</td>
</tr>
<tr>
	<td align = "center">**A115** combing hair</td>
	<td align = "center">**A116** playing hand clapping games</td>
	<td align = "center">**A117** playing trombone</td>
</tr>
<tr>
	<td align = "center">**A118** clam digging</td>
	<td align = "center">**A119** slacklining</td>
	<td align = "center">**A120** climbing tree</td>
</tr>
<tr>
	<td align = "center">**A121** walking on stilts</td>
	<td align = "center">**A122** eating watermelon</td>
	<td align = "center">**A123** squat</td>
</tr>
<tr>
	<td align = "center">**A124** skiing crosscountry</td>
	<td align = "center">**A125** ice skating</td>
	<td align = "center">**A126** falling off bike</td>
</tr>
<tr>
	<td align = "center">**A127** krumping</td>
	<td align = "center">**A128** punching bag</td>
	<td align = "center">**A129** directing traffic</td>
</tr>
<tr>
	<td align = "center">**A130** playing badminton</td>
	<td align = "center">**A131** backflip (human)</td>
	<td align = "center">**A132** bouncing ball (not juggling)</td>
</tr>
<tr>
	<td align = "center">**A133** fencing (sport)</td>
	<td align = "center">**A134** hugging (not baby)</td>
	<td align = "center">**A135** mountain climber (exercise)</td>
</tr>
<tr>
	<td align = "center">**A136** passing American football (not in game)</td>
	<td align = "center">**A137** playing saxophone</td>
	<td align = "center">**A138** pulling rope (game)</td>
</tr>
<tr>
	<td align = "center">**A139** punching person (boxing)</td>
	<td align = "center">**A140** riding camel</td>
	<td align = "center">**A141** riding unicycle</td>
</tr>
<tr>
	<td align = "center">**A142** rock climbing</td>
	<td align = "center">**A143** roller skating</td>
	<td align = "center">**A144** salsa dancing</td>
</tr>
<tr>
	<td align = "center">**A145** shooting goal (soccer)</td>
	<td align = "center">**A146** tango dancing</td>
	<td align = "center">**A147** tap dancing</td>
</tr>
<tr>
	<td align = "center">**A148** tapping guitar</td>
	<td align = "center">**A149** trimming shrubs</td>
	<td align = "center">**A150** using a sledge hammer</td>
</tr>
<tr>
	<td align = "center">**A151** wrestling</td>
	<td align = "center">**A152** zumba</td>
</tr>
</table>
