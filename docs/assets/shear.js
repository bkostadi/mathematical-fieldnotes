/* The horizontal shear sends (cos t, sin t) to (cos t + k sin t, sin t). */
function startShearLab(figure) {
  const canvas = figure.querySelector("canvas");
  const ctx = canvas.getContext("2d");
  if (!ctx) return;

  const stage = figure.querySelector(".shear-stage");
  const slider = figure.querySelector("input");
  const output = figure.querySelector("output");
  const circle = Array.from({ length: 241 }, (_, i) => {
    const t = 2 * Math.PI * i / 240;
    return [Math.cos(t), Math.sin(t)];
  });

  function draw() {
    const width = stage.clientWidth;
    const height = stage.clientHeight;
    if (width < 1 || height < 1) return;

    const k = Number(slider.value);
    const ratio = window.devicePixelRatio || 1;
    canvas.width = Math.round(width * ratio);
    canvas.height = Math.round(height * ratio);
    ctx.setTransform(canvas.width / width, 0, 0, canvas.height / height, 0, 0);

    const scale = height / 2.58;
    const cx = width / 2;
    const cy = height / 2;
    const px = x => cx + scale * x;
    const py = y => cy - scale * y;

    function line(x1, y1, x2, y2, color, weight) {
      ctx.beginPath();
      ctx.strokeStyle = color;
      ctx.lineWidth = weight;
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.stroke();
    }

    ctx.fillStyle = "#173e38";
    ctx.fillRect(0, 0, width, height);
    for (let i = -12; i <= 12; i++) {
      const p = i / 4;
      const shade = i % 2 === 0 ? "#30564d" : "#254a42";
      line(px(p), 0, px(p), height, shade, 0.65);
      line(0, py(p), width, py(p), shade, 0.65);
    }
    line(0, cy, width, cy, "#6a8b7d", 0.85);
    line(cx, 0, cx, height, "#6a8b7d", 0.85);
    ctx.fillStyle = "#c4d6c9";
    ctx.font = "italic 12px Georgia, serif";
    ctx.fillText("x", width - 12, cy - 5);
    ctx.fillText("y", cx + 5, 12);

    function ellipse(shear, color, weight, dashes = []) {
      ctx.beginPath();
      ctx.setLineDash(dashes);
      ctx.strokeStyle = color;
      ctx.lineWidth = weight;
      circle.forEach(([x, y], i) => {
        const sx = px(x + shear * y);
        if (i === 0) ctx.moveTo(sx, py(y));
        else ctx.lineTo(sx, py(y));
      });
      ctx.closePath();
      ctx.stroke();
      ctx.setLineDash([]);
    }

    for (let i = 1; i < 13; i++) ellipse(k * i / 13, "#709688", 0.85);
    ellipse(k, "#ffb384", 2.15);
    ellipse(0, "#f5ecd6", 1.45, [4, 4]);
    ctx.beginPath();
    ctx.arc(px(k), py(1), 4, 0, 2 * Math.PI);
    ctx.fillStyle = "#ffb384";
    ctx.fill();

    const value = k.toFixed(2);
    output.value = value.replace("-", "−");
    slider.setAttribute("aria-valuetext", value);
    canvas.setAttribute("aria-label",
      "Horizontal shear " + value + ". The top point (0, 1) moves to (" +
      value + ", 1). The area stays the same.");
  }

  canvas.hidden = false;
  figure.querySelector(".shear-fallback").hidden = true;
  figure.querySelector(".shear-controls").hidden = false;
  slider.addEventListener("input", draw);
  if (typeof ResizeObserver === "function") {
    new ResizeObserver(draw).observe(stage);
  } else {
    window.addEventListener("resize", draw);
  }
  draw();
}

document.querySelectorAll("[data-shear-lab]").forEach(startShearLab);
