/* Social Media — small progressive enhancements. Everything works without JS. */
(function () {
  "use strict";

  /* ---------- Toasts: auto-dismiss, pause on hover / hidden tab ---------- */
  function dismiss(toast) {
    if (toast.classList.contains("is-leaving")) return;
    toast.classList.add("is-leaving");
    toast.addEventListener("transitionend", function () { toast.remove(); }, { once: true });
    setTimeout(function () { toast.remove(); }, 400);
  }

  document.querySelectorAll("[data-toast]").forEach(function (toast) {
    var remaining = toast.getAttribute("role") === "alert" ? 8000 : 5000;
    var started = Date.now();
    var timer = setTimeout(function () { dismiss(toast); }, remaining);

    function pause() {
      clearTimeout(timer);
      remaining -= Date.now() - started;
    }
    function resume() {
      started = Date.now();
      clearTimeout(timer);
      timer = setTimeout(function () { dismiss(toast); }, Math.max(remaining, 1500));
    }

    toast.addEventListener("mouseenter", pause);
    toast.addEventListener("mouseleave", resume);
    toast.addEventListener("focusin", pause);
    toast.addEventListener("focusout", resume);
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) pause(); else resume();
    });
    var close = toast.querySelector("[data-toast-close]");
    if (close) close.addEventListener("click", function () { dismiss(toast); });
  });

  /* ---------- Account menu: close on outside click / Escape ---------- */
  document.querySelectorAll("[data-menu]").forEach(function (menu) {
    document.addEventListener("click", function (e) {
      if (menu.open && !menu.contains(e.target)) menu.open = false;
    });
    menu.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.open) {
        menu.open = false;
        menu.querySelector("summary").focus();
      }
    });
  });

  /* ---------- Dialogs ---------- */
  document.querySelectorAll("[data-open-dialog]").forEach(function (btn) {
    var dialog = document.getElementById(btn.getAttribute("data-open-dialog"));
    if (!dialog || typeof dialog.showModal !== "function") return;
    btn.addEventListener("click", function () {
      dialog.showModal();
      var first = dialog.querySelector("textarea, input:not([type=hidden])");
      if (first) first.focus();
    });
    dialog.addEventListener("click", function (e) {
      if (e.target === dialog) dialog.close();
    });
  });
  document.querySelectorAll("[data-close-dialog]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var dialog = btn.closest("dialog");
      if (dialog) dialog.close();
    });
  });

  /* ---------- Forms: prevent double submit, show busy state ---------- */
  document.querySelectorAll("form").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      if (form.dataset.submitting === "1") { e.preventDefault(); return; }
      form.dataset.submitting = "1";
      var btn = e.submitter || form.querySelector("[type=submit]");
      if (btn) {
        btn.setAttribute("aria-busy", "true");
        btn.classList.add("is-busy");
      }
      // Pages restored from bfcache must be submittable again.
      window.addEventListener("pageshow", function () {
        form.dataset.submitting = "";
        if (btn) { btn.removeAttribute("aria-busy"); btn.classList.remove("is-busy"); }
      }, { once: true });
    });
  });

  /* ---------- File inputs: preview chosen image ---------- */
  document.querySelectorAll('input[type="file"]').forEach(function (input) {
    input.addEventListener("change", function () {
      var file = input.files && input.files[0];
      var holder = input.parentElement.querySelector(".file-preview");
      if (!file || !file.type.startsWith("image/")) {
        if (holder) holder.remove();
        return;
      }
      if (!holder) {
        holder = document.createElement("img");
        holder.className = "file-preview";
        holder.alt = "";
        input.insertAdjacentElement("afterend", holder);
      }
      if (holder.dataset.url) URL.revokeObjectURL(holder.dataset.url);
      holder.dataset.url = URL.createObjectURL(file);
      holder.src = holder.dataset.url;
    });
  });

  /* ---------- Placeholders the server forms don't set ---------- */
  var search = document.querySelector('.search-bar input[name="search"]');
  if (search && !search.placeholder) search.placeholder = "Search by username";
  var comment = document.querySelector('.comment-compose textarea');
  if (comment && !comment.placeholder) comment.placeholder = "Write a comment";
  var repostText = document.querySelector('dialog textarea');
  if (repostText && !repostText.placeholder) repostText.placeholder = "Add a note (optional)";

  /* ---------- Textareas: grow with content ---------- */
  document.querySelectorAll("textarea[data-autogrow], .comment-compose textarea, dialog textarea").forEach(function (ta) {
    function fit() {
      ta.style.height = "auto";
      ta.style.height = Math.min(ta.scrollHeight + 2, 420) + "px";
    }
    ta.addEventListener("input", fit);
  });
})();
