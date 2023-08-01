Flask App with Translation and User Login Emulation

This repository contains a simple Flask app that demonstrates how to implement translation (internationalization) using Flask-Babel and how to emulate a user login system. The app allows users to view the current time in their preferred time zone and displays a welcome message based on their preferred locale.

Installation

To run the app, you need to have Python and Flask installed. Additionally, you need to install the required dependencies using pip

Features
The Flask app includes the following features:

Translation (Internationalization):

 The app uses Flask-Babel to handle translation of messages into different languages. The available languages are English and French, and the app is set to English ("en") by default. You can change the language to French ("fr") by adding the ?locale=fr parameter to the URL. The app will display messages and date formats in the selected language.

Emulated User Login: 

The app emulates a user login system by using a mock user table stored in the users dictionary. Users can be "logged in" by adding the ?login_as=user_id parameter to the URL. The app will fetch the user's preferred locale and time zone from the user table and display the welcome message and current time accordingly.

Preferred Time Zone: 

The app displays the current time in the user's preferred time zone, which can be specified using the timezone parameter in the URL. If the user is logged in and has a valid preferred time zone, the app will display the time accordingly. Otherwise, it will use the default time zone (UTC).

Routes

/: The home page of the app. It displays a welcome message and the current time in the user's preferred time zone.

Testing Different Users and Translations

To test different users and translations, you can access the app with the following URL parameters:

Conclusion

This Flask app demonstrates how to implement translation and user login emulation using Flask-Babel. It allows users to view the current time in their preferred time zone and displays messages in their preferred language.
