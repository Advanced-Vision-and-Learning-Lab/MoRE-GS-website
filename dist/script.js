document.querySelectorAll('[data-copy]').forEach((button) => {
  button.addEventListener('click', async () => {
    const source = document.getElementById(button.dataset.copy);
    if (!source) return;
    try {
      await navigator.clipboard.writeText(source.innerText);
      const previous = button.textContent;
      button.textContent = 'Copied';
      window.setTimeout(() => { button.textContent = previous; }, 1600);
    } catch {
      button.textContent = 'Select and copy';
    }
  });
});

const dialog = document.querySelector('[data-lightbox-dialog]');
const dialogImage = document.querySelector('[data-lightbox-image]');

if (dialog && dialogImage) {
  document.querySelectorAll('[data-lightbox]').forEach((button) => {
    button.addEventListener('click', () => {
      dialogImage.src = button.dataset.lightbox;
      dialogImage.alt = button.querySelector('img')?.alt || '';
      dialog.showModal();
    });
  });
  document.querySelector('[data-lightbox-close]')?.addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', (event) => {
    if (event.target === dialog) dialog.close();
  });
}

const compare = document.querySelector('[data-compare]');

if (compare) {
  const range = compare.querySelector('[data-compare-range]');
  const base = compare.querySelector('[data-compare-base]');
  const top = compare.querySelector('[data-compare-top]');
  range.addEventListener('input', () => {
    compare.style.setProperty('--split', `${range.value}%`);
  });
  const tabs = document.querySelectorAll('.compare-tabs [data-base]');
  tabs.forEach((tab) => {
    tab.addEventListener('click', () => {
      tabs.forEach((other) => other.setAttribute('aria-selected', String(other === tab)));
      base.src = tab.dataset.base;
      top.src = tab.dataset.top;
    });
  });
}

if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  document.querySelectorAll('video[autoplay]').forEach((video) => video.pause());
}
