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
    <td>125,657</td>
  </tr>
</table>
</center>

### Downalod Dataset

Skeletics 152 dataset can be downloaded from this <a href = "https://skeleton.iiit.ac.in/skeletics-152-data">link</a>

A .zip file will be downloaded from this link which will contain, two more .zip files:
1. vibe_results_train.zip
2. vibe_results_val.zip

Which contains VIBE skeleton results for train and validation split respecitvely.

Inside each of these .zip files there will be folders with the name of different classes and inside each folder there will be json files containing VIBE skeleon results for different video samples in that class.

### Dataset preparation

To obtain 3d skeletons from the RGB video, [VIBE pose estimation model](https://github.com/mkocabas/VIBE) is used. VIBE pose estimate gives 49 joints in total out of which we are choosing the first <b>25</b>
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


### Class Labels (152 classes)

<table>

<tr>
	<td align = "center"><b>A1</b> tai chi</td>
	<td align = "center"><b>A2</b> walking with crutches</td>
	<td align = "center"><b>A3</b> juggling soccer ball</td>
</tr>
<tr>
	<td align = "center"><b>A4</b> dribbling basketball</td>
	<td align = "center"><b>A5</b> catching or throwing softball</td>
	<td align = "center"><b>A6</b> playing organ</td>
</tr>
<tr>
	<td align = "center"><b>A7</b> catching or throwing baseball</td>
	<td align = "center"><b>A8</b> taking photo</td>
	<td align = "center"><b>A9</b> robot dancing</td>
</tr>
<tr>
	<td align = "center"><b>A10</b> playing cello</td>
	<td align = "center"><b>A11</b> training dog</td>
	<td align = "center"><b>A12</b> tiptoeing</td>
</tr>
<tr>
	<td align = "center"><b>A13</b> pumping fist</td>
	<td align = "center"><b>A14</b> contact juggling</td>
	<td align = "center"><b>A15</b> skipping stone</td>
</tr>
<tr>
	<td align = "center"><b>A16</b> playing piccolo</td>
	<td align = "center"><b>A17</b> front raises</td>
	<td align = "center"><b>A18</b> dancing gangnam style</td>
</tr>
<tr>
	<td align = "center"><b>A19</b> head stand</td>
	<td align = "center"><b>A20</b> side kick</td>
	<td align = "center"><b>A21</b> push up</td>
</tr>
<tr>
	<td align = "center"><b>A22</b> riding a bike</td>
	<td align = "center"><b>A23</b> stretching arm</td>
	<td align = "center"><b>A24</b> bench pressing</td>
</tr>
<tr>
	<td align = "center"><b>A25</b> casting fishing line</td>
	<td align = "center"><b>A26</b> disc golfing</td>
	<td align = "center"><b>A27</b> playing accordion</td>
</tr>
<tr>
	<td align = "center"><b>A28</b> playing ping pong</td>
	<td align = "center"><b>A29</b> air drumming</td>
	<td align = "center"><b>A30</b> chopping wood</td>
</tr>
<tr>
	<td align = "center"><b>A31</b> country line dancing</td>
	<td align = "center"><b>A32</b> tightrope walking</td>
	<td align = "center"><b>A33</b> catching or throwing frisbee</td>
</tr>
<tr>
	<td align = "center"><b>A34</b> exercising with an exercise ball</td>
	<td align = "center"><b>A35</b> riding mechanical bull</td>
	<td align = "center"><b>A36</b> rope pushdown</td>
</tr>
<tr>
	<td align = "center"><b>A37</b> digging</td>
	<td align = "center"><b>A38</b> situp</td>
	<td align = "center"><b>A39</b> shearing sheep</td>
</tr>
<tr>
	<td align = "center"><b>A40</b> breaking boards</td>
	<td align = "center"><b>A41</b> playing guitar</td>
	<td align = "center"><b>A42</b> golf driving</td>
</tr>
<tr>
	<td align = "center"><b>A43</b> playing drums</td>
	<td align = "center"><b>A44</b> riding mule</td>
	<td align = "center"><b>A45</b> playing ukulele</td>
</tr>
<tr>
	<td align = "center"><b>A46</b> hula hooping</td>
	<td align = "center"><b>A47</b> javelin throw</td>
	<td align = "center"><b>A48</b> singing</td>
</tr>
<tr>
	<td align = "center"><b>A49</b> clapping</td>
	<td align = "center"><b>A50</b> snatch weight lifting</td>
	<td align = "center"><b>A51</b> snorkeling</td>
</tr>
<tr>
	<td align = "center"><b>A52</b> golf chipping</td>
	<td align = "center"><b>A53</b> clean and jerk</td>
	<td align = "center"><b>A54</b> sweeping floor</td>
</tr>
<tr>
	<td align = "center"><b>A55</b> passing soccer ball</td>
	<td align = "center"><b>A56</b> long jump</td>
	<td align = "center"><b>A57</b> playing harp</td>
</tr>
<tr>
	<td align = "center"><b>A58</b> tackling</td>
	<td align = "center"><b>A59</b> skiing slalom</td>
	<td align = "center"><b>A60</b> playing field hockey</td>
</tr>
<tr>
	<td align = "center"><b>A61</b> golf putting</td>
	<td align = "center"><b>A62</b> playing harmonica</td>
	<td align = "center"><b>A63</b> swinging on something</td>
</tr>
<tr>
	<td align = "center"><b>A64</b> longboarding</td>
	<td align = "center"><b>A65</b> jumping into pool</td>
	<td align = "center"><b>A66</b> snowboarding</td>
</tr>
<tr>
	<td align = "center"><b>A67</b> bowling</td>
	<td align = "center"><b>A68</b> shoot dance</td>
	<td align = "center"><b>A69</b> saluting</td>
</tr>
<tr>
	<td align = "center"><b>A70</b> deadlifting</td>
	<td align = "center"><b>A71</b> jumping jacks</td>
	<td align = "center"><b>A72</b> bouncing on bouncy castle</td>
</tr>
<tr>
	<td align = "center"><b>A73</b> playing squash or racquetball</td>
	<td align = "center"><b>A74</b> shot put</td>
	<td align = "center"><b>A75</b> yoga</td>
</tr>
<tr>
	<td align = "center"><b>A76</b> falling off chair</td>
	<td align = "center"><b>A77</b> playing tennis</td>
	<td align = "center"><b>A78</b> swinging baseball bat</td>
</tr>
<tr>
	<td align = "center"><b>A79</b> moon walking</td>
	<td align = "center"><b>A80</b> archery</td>
	<td align = "center"><b>A81</b> stretching leg</td>
</tr>
<tr>
	<td align = "center"><b>A82</b> checking watch</td>
	<td align = "center"><b>A83</b> climbing a rope</td>
	<td align = "center"><b>A84</b> pull ups</td>
</tr>
<tr>
	<td align = "center"><b>A85</b> tobogganing</td>
	<td align = "center"><b>A86</b> hitting baseball</td>
	<td align = "center"><b>A87</b> pushing cart</td>
</tr>
<tr>
	<td align = "center"><b>A88</b> paragliding</td>
	<td align = "center"><b>A89</b> running on treadmill</td>
	<td align = "center"><b>A90</b> high fiving</td>
</tr>
<tr>
	<td align = "center"><b>A91</b> cumbia</td>
	<td align = "center"><b>A92</b> battle rope training</td>
	<td align = "center"><b>A93</b> playing oboe</td>
</tr>
<tr>
	<td align = "center"><b>A94</b> sword swallowing</td>
	<td align = "center"><b>A95</b> biking through snow</td>
	<td align = "center"><b>A96</b> playing violin</td>
</tr>
<tr>
	<td align = "center"><b>A97</b> jogging</td>
	<td align = "center"><b>A98</b> opening door</td>
	<td align = "center"><b>A99</b> chiseling stone</td>
</tr>
<tr>
	<td align = "center"><b>A100</b> abseiling</td>
	<td align = "center"><b>A101</b> hammer throw</td>
	<td align = "center"><b>A102</b>  standing on hands</td>
</tr>
<tr>
	<td align = "center"><b>A103</b> sword fighting</td>
	<td align = "center"><b>A104</b> dunking basketball</td>
	<td align = "center"><b>A105</b> reading book</td>
</tr>
<tr>
	<td align = "center"><b>A106</b> jumpstyle dancing</td>
	<td align = "center"><b>A107</b> cutting cake</td>
	<td align = "center"><b>A108</b> belly dancing</td>
</tr>
<tr>
	<td align = "center"><b>A109</b> exercising arm</td>
	<td align = "center"><b>A110</b> pushing wheelbarrow</td>
	<td align = "center"><b>A111</b> pushing car</td>
</tr>
<tr>
	<td align = "center"><b>A112</b> lunge</td>
	<td align = "center"><b>A113</b> hopscotch</td>
	<td align = "center"><b>A114</b> ski ballet</td>
</tr>
<tr>
	<td align = "center"><b>A115</b> combing hair</td>
	<td align = "center"><b>A116</b> playing hand clapping games</td>
	<td align = "center"><b>A117</b> playing trombone</td>
</tr>
<tr>
	<td align = "center"><b>A118</b> clam digging</td>
	<td align = "center"><b>A119</b> slacklining</td>
	<td align = "center"><b>A120</b> climbing tree</td>
</tr>
<tr>
	<td align = "center"><b>A121</b> walking on stilts</td>
	<td align = "center"><b>A122</b> eating watermelon</td>
	<td align = "center"><b>A123</b> squat</td>
</tr>
<tr>
	<td align = "center"><b>A124</b> skiing crosscountry</td>
	<td align = "center"><b>A125</b> ice skating</td>
	<td align = "center"><b>A126</b> falling off bike</td>
</tr>
<tr>
	<td align = "center"><b>A127</b> krumping</td>
	<td align = "center"><b>A128</b> punching bag</td>
	<td align = "center"><b>A129</b> directing traffic</td>
</tr>
<tr>
	<td align = "center"><b>A130</b> playing badminton</td>
	<td align = "center"><b>A131</b> backflip (human)</td>
	<td align = "center"><b>A132</b> bouncing ball (not juggling)</td>
</tr>
<tr>
	<td align = "center"><b>A133</b> fencing (sport)</td>
	<td align = "center"><b>A134</b> hugging (not baby)</td>
	<td align = "center"><b>A135</b> mountain climber (exercise)</td>
</tr>
<tr>
	<td align = "center"><b>A136</b> passing American football (not in game)</td>
	<td align = "center"><b>A137</b> playing saxophone</td>
	<td align = "center"><b>A138</b> pulling rope (game)</td>
</tr>
<tr>
	<td align = "center"><b>A139</b> punching person (boxing)</td>
	<td align = "center"><b>A140</b> riding camel</td>
	<td align = "center"><b>A141</b> riding unicycle</td>
</tr>
<tr>
	<td align = "center"><b>A142</b> rock climbing</td>
	<td align = "center"><b>A143</b> roller skating</td>
	<td align = "center"><b>A144</b> salsa dancing</td>
</tr>
<tr>
	<td align = "center"><b>A145</b> shooting goal (soccer)</td>
	<td align = "center"><b>A146</b> tango dancing</td>
	<td align = "center"><b>A147</b> tap dancing</td>
</tr>
<tr>
	<td align = "center"><b>A148</b> tapping guitar</td>
	<td align = "center"><b>A149</b> trimming shrubs</td>
	<td align = "center"><b>A150</b> using a sledge hammer</td>
</tr>
<tr>
	<td align = "center"><b>A151</b> wrestling</td>
	<td align = "center"><b>A152</b> zumba</td>
</tr>
</table>
