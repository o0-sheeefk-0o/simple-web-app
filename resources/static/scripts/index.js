const body = document.querySelector("body");
const circle = document.querySelector(".circle");
circle.addEventListener("click", async () => {
  body.classList.toggle("anime");
  await fetch("/time-format", {
    method: "POST",
    body: JSON.stringify({ "time-formatted": "2025-11-29" }),
  })
    .then((res) => res.json)
    .then((data) => console.log(data))
    .catch((err) => console.error(err));
});
