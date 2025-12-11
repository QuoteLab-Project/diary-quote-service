document.querySelector("#loginForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const form = e.target;
    const data = {
        email: form.email.value,
        password: form.password.value
    };

    const res = await fetch("/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    if (res.ok) {
        const token = (await res.json()).access_token;
        localStorage.setItem("token", token);
        window.location.href = "/home";
    } else {
        alert("로그인 실패");
    }
});
