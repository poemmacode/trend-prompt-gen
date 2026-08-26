const form = document.getElementById("trend-form");
const results = document.getElementById("results");
const reportContent = document.getElementById("report-content");
const errorDiv = document.getElementById("error");
const submitBtn = document.getElementById("submit-btn");
const btnText = document.getElementById("btn-text");
const btnLoading = document.getElementById("btn-loading");
const copyBtn = document.getElementById("copy-btn");

function showError(msg) {
  errorDiv.textContent = msg;
  errorDiv.classList.remove("hidden");
}

function hideError() {
  errorDiv.classList.add("hidden");
}

function setLoading(loading) {
  submitBtn.disabled = loading;
  btnText.classList.toggle("hidden", loading);
  btnLoading.classList.toggle("hidden", !loading);
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  hideError();
  results.classList.add("hidden");

  const niche = document.getElementById("niche").value.trim();
  const apiKey = document.getElementById("api-key").value.trim();

  if (!niche || !apiKey) {
    showError("Please fill in both fields.");
    return;
  }

  setLoading(true);

  try {
    const params = new URLSearchParams({ niche });
    const res = await fetch(`/api/v1/report?${params.toString()}`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
      },
    });

    const data = await res.json();

    if (!res.ok) {
      showError(data.detail || `Error ${res.status}`);
      return;
    }

    reportContent.textContent = data.report;
    results.classList.remove("hidden");
  } catch (err) {
    showError("Network error. Please try again.");
  } finally {
    setLoading(false);
  }
});

copyBtn.addEventListener("click", () => {
  const text = reportContent.textContent;
  navigator.clipboard.writeText(text).then(() => {
    copyBtn.textContent = "Copied!";
    setTimeout(() => {
      copyBtn.textContent = "Copy report";
    }, 2000);
  });
});
