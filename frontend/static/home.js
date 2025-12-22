// ------------------------------
// 공통: Authorization 헤더 생성
// ------------------------------
function authHeaders() {
    const token = localStorage.getItem("token");
    return {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
    };
}

// ------------------------------
// 로그인 사용자 정보 불러오기
// ------------------------------
async function loadUser() {
    const res = await fetch("/auth/me", { headers: authHeaders() });

    if (!res.ok) return;

    const user = await res.json();
    document.querySelector(".username").innerText = `${user.nickname}님`;
}

// ------------------------------
// 오늘의 질문
// ------------------------------
async function loadQuestion() {
    const res = await fetch("/questions/", { headers: authHeaders() });

    if (!res.ok) {
        document.querySelector("#questionText").innerText = "질문을 가져올 수 없습니다.";
        return;
    }

    const data = await res.json();
    document.querySelector("#questionText").innerText = data.text;
    document.querySelector("#questionCategory").innerText = `카테고리: ${data.category}`;
}

// ------------------------------
// 오늘의 명언
// ------------------------------
async function loadQuote() {
    const res = await fetch("/quotes/random", { headers: authHeaders() });

    if (!res.ok) {
        document.querySelector("#quoteContent").innerText = "명언을 가져올 수 없습니다.";
        return;
    }

    const data = await res.json();
    document.querySelector("#quoteContent").innerText = data.content;
    document.querySelector("#quoteAuthor").innerText = `- ${data.author}`;
}

// ------------------------------
// 일기 저장
// ------------------------------
async function saveDiary() {
    const title = document.querySelector("#diaryTitle").value;
    const text = document.querySelector("#diaryContent").value;

    if (!title || !text) {
        alert("제목과 내용을 입력하세요.");
        return;
    }

    const res = await fetch("/diary/", {
        method: "POST",
        headers: authHeaders(),
        body: JSON.stringify({ title, text })
    });

    if (res.ok) {
        alert("일기가 저장되었습니다!");
        document.querySelector("#diaryTitle").value = "";
        document.querySelector("#diaryContent").value = "";
        loadRecentDiaries();
    }
}

// ------------------------------
// 최근 일기 불러오기 (날짜 + 시간 포함)
// ------------------------------
async function loadRecentDiaries() {
    const res = await fetch("/diary/", { headers: authHeaders() });
    if (!res.ok) return;

    const diaries = await res.json();
    const list = document.querySelector("#diaryList");
    list.innerHTML = "";

    diaries.slice(0, 5).forEach(d => {
        const dateObj = new Date(d.created_at);
        const formatted =
            `${dateObj.getFullYear()}-${String(dateObj.getMonth() + 1).padStart(2, "0")}-${String(dateObj.getDate()).padStart(2, "0")} ` +
            `${String(dateObj.getHours()).padStart(2, "0")}:${String(dateObj.getMinutes()).padStart(2, "0")}`;

        const li = document.createElement("li");
        li.innerHTML = `
            <div class="diary-header">
                <strong>${d.title}</strong>
                <span class="diary-date">${formatted}</span>
            </div>
            <p>${d.text.substring(0, 40)}...</p>
        `;
        list.appendChild(li);
    });
}

// ------------------------------
// 로그아웃
// ------------------------------
document.querySelector("#logoutBtn").addEventListener("click", async () => {
    await fetch("/auth/logout", {
        method: "POST",
        headers: authHeaders(),
    });

    localStorage.removeItem("token");
    window.location.href = "/login";
});

// ------------------------------
// 버튼 이벤트
// ------------------------------
document.querySelector("#newQuestionBtn").addEventListener("click", loadQuestion);
document.querySelector("#newQuoteBtn").addEventListener("click", loadQuote);
document.querySelector("#saveDiaryBtn").addEventListener("click", saveDiary);

// ------------------------------
// 초기 데이터 로드
// ------------------------------
loadUser();
loadQuestion();
loadQuote();
loadRecentDiaries();
