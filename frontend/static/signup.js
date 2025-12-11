document.querySelector("#signupForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const form = e.target;

    const data = {
        email: form.email.value,
        nickname: form.nickname.value,
        password: form.password.value
    };

    const res = await fetch("/auth/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    if (res.ok) {
        alert("회원가입 성공!");
        window.location.href = "/login";
    } else {
        alert("회원가입 실패");
    }
});
