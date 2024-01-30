// FirebaseUI config
const uiConfig = {
    signInSuccessUrl: '/welcome/',
    signInOptions: [
        // Add your preferred authentication providers here (e.g., Google, Email/Password)
        firebase.auth.EmailAuthProvider.PROVIDER_ID,
    ],
};

// Initialize the FirebaseUI Widget using Firebase
const ui = new firebaseui.auth.AuthUI(firebase.auth());
ui.start('#firebaseui-auth-container', uiConfig);
