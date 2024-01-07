# Tier List Video Generator

### This python program automates the process of making a top 10/top 100/top 1000 etc. video by utilizing the OpenCV library.

## Requirements

OpenCV, NumPy and OS. These can be installed with either PIP or Brew

## Usage

- Download the files (duh)
- Add input and output folders
- Make sure they are all in the same folder, they are correctly named, and that there are no duplicates
- Set the configuration (more about this in the _customization_ section)
- Run the generator
- The result will be added to the output folder

## Customization

This generator comes with many customization features, these include:

- Change background and text color
- Change framerate
- Change resolution
- Change speed of transitions
- Add custom images
- Use of any OpenCV font
- Change the speed of transitions

While most of these are set in the first few lines of the script, some are located within the functions.

## Limitations

Although I have spent many hours on this project, I have not yet implemented some features, these include: special characters, custom fonts, and custom sounds/music. I do hope I can finish these in the near future.

## Suggested settings

Even the you can customize a lot of settings, doesn't mean that it will always work properly. For that reason I have provided below the settings I have found to work the best.

- 720p resolution (1280x720)
- 24 frames per second
- 12 transition frames

## Extra resources

**RESOLUTIONS:**

- 2160p = 3840x2160
- 1440p = 2560×1440
- 1080p = 1920×1080
- 720p = 1280×720
- 480p = 640×480
- 360p = 480×360
- 240p = 426×240
- 144p = 256×144

**FRAMERATE:**

- 24 - 60

**OpenCV Fonts**

- FONT_HERSHEY_SIMPLEX = 0
- FONT_HERSHEY_PLAIN = 1
- FONT_HERSHEY_DUPLEX = 2
- FONT_HERSHEY_COMPLEX = 3
- FONT_HERSHEY_TRIPLEX = 4
- FONT_HERSHEY_COMPLEX_SMALL = 5
- FONT_HERSHEY_SCRIPT_SIMPLEX = 6
- FONT_HERSHEY_SCRIPT_COMPLEX = 7

## More about this project and its future

I was inspired to make this project after sitting through the entirety of "Top 1000 Cheese". I wanted this to be a simple way to recreate the original. While it is not 100% accurate (different font different resolution, etc.) I still think I did a good job, seeing as this is my first time working with OpenCV. Fun fact: This project was originally meant to be written in MoviePy before I figured out its limitations. If you want to view some test outputs from this project, you can view them on the youtube channel below (not my main channel). In the future I want to implement other tools apart from OpenCV (like pillow) to help fix some visual issues connected with text displaying and to support custom fonts.

https://www.youtube.com/@testoutputfiles

## Disclaimer and License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This code is licensed under MIT. The full license is included in the _LICENSE_ file.
