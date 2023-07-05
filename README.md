# Drowsiness Detection Model

The **Drowsiness Detection Model** is a project that utilizes computer vision techniques and machine learning to detect drowsiness in individuals. The project makes use of the OpenCV library for computer vision tasks and TensorFlow with Keras for building and training the machine learning model. It is deployed using Streamlit for a user-friendly interface.

## Requirements

To run the Drowsiness Detection Model project, you need to have the following software and libraries installed:

1. **Python**: The project is written in Python, so you need to have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

2. **Dependencies**: The required dependencies for the project are listed in the `requirements.txt` file. You can install them by running the following command:


## Usage

1. Clone the repository or download the project files to your local machine.

2. Install the required dependencies mentioned in the "Requirements" section by running the command mentioned above.

3. Open a terminal or command prompt and navigate to the project directory.

4. Run the following command to start the drowsiness detection model using Streamlit:



5. The application will open in your default web browser, displaying the user interface for the drowsiness detection model.

6. Follow the instructions provided by the application to use the webcam for video capture and detect drowsiness.

## Output Examples

### Eyes Closed

When the model detects closed eyes, it generates an alert message. Here is an example output:

![Eyes Closed](images/eyes_closed.jpg)

### Eyes Open

When the model detects open eyes, it does not generate an alert. Here is an example output:

![Eyes Open](images/eyes_open.jpg)

## Customization

You can customize the Drowsiness Detection Model according to your requirements. Here are a few suggestions:

- **Model Training**: If you have a custom dataset, you can train your own drowsiness detection model using TensorFlow and Keras. You can explore different architectures, hyperparameters, and training techniques to improve the model's performance.

- **User Interface**: The Streamlit application provides a basic user interface. You can enhance and customize the interface by modifying the `drowsiness_detection_app.py` file. You can add additional features, buttons, or instructions to make the user experience more interactive.

- **Integration**: The Drowsiness Detection Model can be integrated into other applications or systems. You can extract the relevant code and integrate it into your own projects, such as a driver assistance system or a monitoring application.

## Contributing

If you'd like to contribute to the Drowsiness Detection Model project, you can fork the repository, make improvements or add new features, and submit a pull request.

Please ensure that your code follows the project's coding style and conventions. Additionally, include appropriate tests and update the documentation if necessary.

## License

The Drowsiness Detection Model project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for both commercial and non-commercial purposes.
