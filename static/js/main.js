function setupContactForm() {
  const form = document.getElementById("contactForm");
  const statusEl = document.getElementById("formStatus");
  if (!form) return;

  function setStatus(msg) {
    if (statusEl) statusEl.textContent = msg;
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    setStatus("Sending…");

    const fd = new FormData(form);

    try {
      const res = await fetch("/api/contact", { method: "POST", body: fd });
      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.error || "Submission failed.");
      form.reset();
      setStatus("Sent. We’ll get back to you shortly.");
    } catch (err) {
      setStatus(err && err.message ? err.message : "Something went wrong.");
    }
  });
}

function setupContactPrefill() {
  const params = new URLSearchParams(window.location.search);
  const service = params.get("service");
  const message = params.get("message");
  if (!service && !message) return;

  const forms = document.querySelectorAll("form");
  forms.forEach((form) => {
    const select = form.querySelector('select[name="service"]');
    if (service && select) {
      const hasOption = Array.from(select.options || []).some((o) => o.value === service);
      if (hasOption) select.value = service;
    }

    const textarea = form.querySelector('textarea[name="message"]');
    if (message && textarea && !textarea.value) {
      textarea.value = message;
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  // Global layout / nav / reveal / year logic is handled inline in base.html
  // to keep templates self-contained. Here we only wire up page-specific
  // behaviours that aren't already managed there.
  setupContactPrefill();
  setupContactForm();
});

