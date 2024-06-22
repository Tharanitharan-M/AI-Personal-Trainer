## AI Personal Trainer with OpenCV and MediaPipe

This repository contains Python code to count the number of bicep curls performed in real-time using OpenCV and MediaPipe.

### Dependencies

This project requires the following Python libraries:

* OpenCV-python
* MediaPipe
* NumPy (optional, for image manipulation)

You can install them using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install all the necessary dependencies in one go.

### Usage

1. Clone this repository.
2. Open a terminal in the project directory.
3. Run the script:

```bash
git clone https://github.com/Tharanitharan-M/AI-Personal-Trainer.git
```

### How it Works

The program utilizes MediaPipe's pose estimation model to track the position of your elbow and shoulder. By analyzing the angle between these joints, it can determine if your arm is in a flexed (curled) or extended position. When the arm transitions from extended to flexed and back again, a bicep curl is counted.

### Further Development

This project serves as a starting point for a real-time bicep curl counter. Here are some ideas for further development:

* Improve accuracy by incorporating background subtraction techniques.
* Add visual cues to highlight the tracked body parts.
* Implement rep tracking for other exercises.
* Create a graphical user interface for a more user-friendly experience.

### License

This project is licensed under the MIT License (see LICENSE file for details).
