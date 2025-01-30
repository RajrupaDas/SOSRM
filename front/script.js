// Import Firebase modules
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, sendEmailVerification } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

// Firebase Configuration
const firebaseConfig = {
    apiKey: "AIzaSyD6prPCCCzSeVgtBaekwT2SYLzbnR4z7N4",
    authDomain: "messaging-39b51.firebaseapp.com",
    projectId: "messaging-39b51",
    storageBucket: "messaging-39b51.firebasestorage.app",
    messagingSenderId: "114428161895",
    appId: "1:114428161895:web:3bf41ed7eeb5f028b989c2",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Sign Up Function
window.signUp = function () {
    const email = document.getElementById("signupEmail").value;
    const password = document.getElementById("signupPassword").value;

    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            const user = userCredential.user;
            sendEmailVerification(user);
            alert("Verification email sent! Check your inbox.");
        })
        .catch((error) => alert(error.message));
};

// Sign In Function with Redirect
window.login = function () {
    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;

    signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            const user = userCredential.user;
            if (user.emailVerified) {
                alert("Login successful! Redirecting...");
                window.location.href = "dashboard.html"; // Redirect after login
            } else {
                alert("Please verify your email first!");
            }
        })
        .catch((error) => alert(error.message));
};
