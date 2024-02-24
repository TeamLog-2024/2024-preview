<template>
  <div class="container">
    <div class="name">Get the TeamLog!</div>

    <div class="player-container">Score Board
      <div id="score">{{ score }}</div>
      <div id="timer">{{ timer }}</div>
    </div>
  
    <div id="game-container">
      <div class="circle" @click="handleClick">
        <img src="https://avatars.githubusercontent.com/u/26594715?s=200&v=4" alt="TeamLog">
      </div>
      <CustomAlert :score="score" :v-show="showModal" @close="closeModal"/>
    </div>

    <div v-if="showAlert" class="custom-alert">
      <div class="overlay"></div>
      <div class="alert-box">
        <h2>Congratulations!</h2>
        <p>You caught TeamLog!</p>
        <p>최종 점수: {{ score }}</p>
        <button @click="hideAlert">Close</button>
      </div>
    </div>
  </div>
</template>


<script>

export default {
  name: 'ClickGame',
  data() {
    return {
      score: 0,
      timer: 30,
      countdown: null,
      showModal:false,
      showAlert: false
    };
  },
  mounted() {
    this.regenerateCircle();
    this.startTimer();
    window.addEventListener("resize", this.regenerateCircle);
  },
  methods: {
    handleClick() {
      this.score++;
      this.regenerateCircle();
    },
    
    regenerateCircle() {
      const gameContainer = document.getElementById("game-container");
      gameContainer.innerHTML = "";

      const newCircle = document.createElement("div");
      newCircle.classList.add("circle");

      const viewportWidth = window.innerWidth || document.documentElement.clientWidth;
      const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
      const maxSize = Math.min(viewportWidth, viewportHeight) * 0.7;
      const circleSize = Math.random() * (maxSize - 70);

      const centerX = (viewportWidth - circleSize) / 2;
      const centerY = (viewportHeight - circleSize) / 2;

      let left = Math.random() * (centerX * 0.8) + (centerX * 0.1);
      let top = Math.random() * (centerY * 0.8) + (centerY * 0.1);

      left = Math.max(0, Math.min(left, viewportWidth - circleSize));
      top = Math.max(0, Math.min(top, viewportHeight - circleSize));

      newCircle.style.left = left + "px";
      newCircle.style.top = top + "px";
      newCircle.style.width = circleSize + "px";
      newCircle.style.height = circleSize + "px";

      const image = document.createElement("img");
      image.src = "https://avatars.githubusercontent.com/u/26594715?s=200&v=4";
      image.alt = "TeamLog";

      newCircle.appendChild(image);
      gameContainer.appendChild(newCircle);

      newCircle.addEventListener("click", this.handleClick);

    },
    startTimer() {
      this.countdown = setInterval(() => {
        this.timer--;

        if (this.timer === 0) {
          clearInterval(this.countdown);
          const circle = document.querySelector(".circle");
          circle.removeEventListener("click", this.handleClick);
          this.showFireworks = true;
          this.showAlert = true;
        }
      }, 1000);
    },
    closeModal() {
        this.showModal = false;
    },
    hideAlert() {
      this.showAlert = false;
    }
  }
};
</script>


<style>
  * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: #f9fafb;
  font-family: 'Poppins', sans-serif;
  overflow: hidden;
}

#game-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 85vh;
}

.circle {
  position: relative;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
  animation: pulse 2s infinite;
  cursor: pointer;
  background-color: #ff6b6b;
}

@keyframes pulse {
  0% {
      transform: scale(1);
  }
  50% {
      transform: scale(1.2);
  }
  100% {
      transform: scale(1);
  }
}

.circle img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.container {
  position: relative;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: flex-start;
}

.name {
  color: #FF7F50;
  font-size: 4vw;
  font-weight: bold;
  margin-bottom: 2vh;
  text-align: center;
  text-transform: uppercase;
  text-shadow: 0.5vw 0.5vw 1vw rgba(0, 0, 0, 0.3);
  font-family: 'Arial Black', sans-serif;
  animation: flutter 0.2s infinite alternate;
  transform: skew(-10deg) translateY(20px);
}

.player-container {
  color: #FF7F50;
  font-size: 1.5vw;
  font-weight: bold;
  text-align: center;
  text-transform: uppercase;
  text-shadow: 0.5vw 0.5vw 1vw rgba(0, 0, 0, 0.3);
  width:30vw;
  height: 20vh;
  padding: 20px;
  background-color: #f2f2f2;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 18%;
  left: 35vw;
}


.name, .player-container {
  position: fixed;
}



#score {
  text-align: center;
  font-size: 36px; 
  font-weight: bold; 
  margin-top: 60px; 
  margin-bottom: 20px; 
  color: #333333;
  background-color: #ffffff;
  padding: 20px; 
  border-radius: 10px; 
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
  display: block;
  margin-left: auto; 
  margin-right: auto;
  height: 10vh;
  width: 10vw; 
  position:fixed;
  top: 18%;
  left: 43%;
  transform: translateX(-50%);
}

#timer {
  text-align: center;
  font-size: 36px; 
  font-weight: bold; 
  margin-top: 20px; 
  margin-bottom: 100px; 
  color: #333333;
  background-color: #ffffff;
  padding: 20px; 
  border-radius: 10px; 
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
  display: block;
  margin-left: auto; 
  margin-right: auto;
  height: 10vh;
  width: 10vw;
  position: absolute; 
  top: 26%; 
  left: 72%; 
  transform: translateX(-50%);
}

.custom-alert {
  position: fixed;
  top: 0;
  left: 0;
  padding:20px;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.5);
}

.alert-box {
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
  text-align: center;
}

.alert-box h2 {
  color: #ff6b6b;
  margin-bottom: 10px;
}

.alert-box p {
  margin-bottom: 10px;
}

.alert-box button {
  padding: 10px 20px;
  background-color: #ff6b6b;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.alert-box button:hover {
  background-color: #ff8989;
}

@keyframes fireworks {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  100% {
    transform: scale(1.5);
    opacity: 1;
  }
}

@media (max-width: 768px) {
  .circle {
      width: 150px;
      height: 150px;
  }

  .player-container {
  color: #FF7F50;
  font-size: 1.5vw;
  font-weight: bold;
  text-align: center;
  text-transform: uppercase;
  text-shadow: 0.5vw 0.5vw 1vw rgba(0, 0, 0, 0.3);
  width:30vw;
  height: 20vh;
  padding: 20px;
  background-color: #f2f2f2;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 10%;
  left: 35vw;
}

  #score {
  text-align: center;
  font-size: 30px; 
  font-weight: bold; 
  margin-top: 60px; 
  margin-bottom: 20px; 
  color: #333333;
  background-color: #ffffff;
  padding: 20px; 
  border-radius: 10px; 
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
  display: block;
  margin-left: auto; 
  margin-right: auto;
  height: 10vh;
  width: 10vw; 
  position: absolute;
  top: -2vh;
  left: 28%;
  transform: translateX(-50%);
}

#timer {
  text-align: center;
  font-size: 30px; 
  font-weight: bold; 
  margin-top: 20px; 
  margin-bottom: 100px; 
  color: #333333;
  background-color: #ffffff;
  padding: 20px; 
  border-radius: 10px; 
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
  display: block;
  margin-left: auto; 
  margin-right: auto;
  height: 10vh;
  width: 10vw;
  position: absolute; 
  top: 4vh; 
  left: 72%; 
  transform: translateX(-50%);
}

}

@media (max-width: 480px) {
  .circle {
      width: 100px;
      height: 100px;
  }

  .player-container {
  color: #FF7F50;
  font-size: 2vw;
  font-weight: bold;
  text-align: center;
  text-transform: uppercase;
  text-shadow: 0.5vw 0.5vw 1vw rgba(0, 0, 0, 0.3);
  width:30vw;
  height: 20vh;
  padding: 20px;
  background-color: #f2f2f2;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 9vh;
  left: 35vw;
}


.name, .player-container {
  position: fixed;
}



#score {
  text-align: center;
  font-size: 25px; 
  font-weight: bold; 
  margin-top: 60px; 
  margin-bottom: 20px; 
  color: #333333;
  background-color: #ffffff;
  padding: 20px; 
  border-radius: 10px; 
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
  display: block;
  margin-left: auto; 
  margin-right: auto;
  height: 10vh;
  width: 10vw; 
  position: absolute;
  top:-2vh;
  left: 28%;
  transform: translateX(-50%);
}

#timer {
  text-align: center;
  font-size: 25px; 
  font-weight: bold; 
  margin-top: 20px; 
  margin-bottom: 100px; 
  color: #333333;
  background-color: #ffffff;
  padding: 20px; 
  border-radius: 10px; 
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
  display: flex;
  justify-content: center;
  margin-left: auto; 
  margin-right: auto;
  height: 10vh;
  width: 10vw;
  position: absolute; 
  top: 4vh; 
  left: 72%; 
  transform: translateX(-50%);
}

}
</style>
  