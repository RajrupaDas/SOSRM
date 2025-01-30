import { getAuth, signOut } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

// Initialize Firebase Auth
const auth = getAuth();

// Logout function
window.logout = function () {
    signOut(auth).then(() => {
        alert("Logged out!");
        window.location.href = "index.html"; // Redirect to login page
    }).catch((error) => {
        alert(error.message);
    });
};


