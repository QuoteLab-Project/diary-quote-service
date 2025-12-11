function authHeaders() {
    const token = localStorage.getItem("token");
    return {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
    };
}

async function loadAllDiaries() {
    const res = await fetch("/diary/", { headers: authHeaders() });

    const list = document.querySelector("#diaryAllList");

    if (!res.ok) {
        list.innerHTML = "<p>일기를 불러올 수 없습니다.</p>";
        return;
    }

    const diaries = await res.json();
    list.innerHTML = "";

    diaries.forEach((d) => {
        const li = document.createElement("li");
        li.classList.add("diary-item");

        li.innerHTML = `
            <h3>${d.title}</h3>
            <p>${d.text}</p>
            <small>${new Date(d.created_at).toLocaleString()}</small>
        `;

        list.appendChild(li);
    });
}

loadAllDiaries();
