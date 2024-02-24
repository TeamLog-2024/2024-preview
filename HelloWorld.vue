<template>
  <div>
    <div class="bubble-container">
      <div v-for="bubble in bubbles" :key="bubble.id" class="bubble" :style="bubble.styles"></div>
    </div>

    <div class="container">
      <h1>WELCOME</h1>
      <form id="login-form" @submit.prevent="start">
        <input id="user" type="text" v-model="username" placeholder="사용자명" required>
        <input id="intro" type="text" v-model="intro" placeholder="한줄소개" required>
        <button class="button" @click="$router.push('/about')">Game START ➜</button>
      </form>
    </div>

  </div>
</template>

<script>

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      bubbles: [],
    };
  },
  mounted() {
    setInterval(this.createBubble, 1000);
  },
  methods: {
    start() {
      this.$router.push({
        name: 'about',
      });
    },
    createBubble() {
      console.log("버블 생성 함수 호출됨");
      const size = Math.floor(Math.random() * 20) + 5;
      const x = Math.random() * 100;
      const y = Math.random() * 100;

      this.bubbles.push({
        id: Date.now(),
        styles: {
          width: size + 'px',
          height: size + 'px',
          left: x + '%',
          top: y + '%'
        }
      });

      setTimeout(() => {
        this.bubbles.shift();
      }, 5000);
    },
  }
};
</script>

<style scoped>
body {
  background-color: #F2F2F2;
  font-family: Arial, sans-serif;
}

h1 {
  color: #FF7F50;
  font-size: 50px;
  margin-bottom: 20px;
  font-family: "Verdana", sans-serif; 
  letter-spacing: 2px; 
  text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.1); 
  position: absolute;
  left: 50%;
  top: 30%;
  transform: translate(-50%, -50%);
}

#login-form {
  display: grid;
  align-items: center;
  justify-content: center;
  place-content: center;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

#user, #intro {
  width: 50%;
  padding: 15px;
  margin-bottom: 15px;
  min-width: 60vh;
  border: 1px solid #CCC;
  border-radius: 5px;
  flex-direction: column;
  position: relative;
  margin-left: auto;
  margin-right: auto;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.button {
  font-family: "Verdana", sans-serif; 
  font-size: 17px;
  background-color: #FF7F50;
  color: #FFF;
  padding: 15px 30px;
  border: 5px;
  border-radius: 5px;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center; 
  position: relative;
  margin-left: auto;
  margin-right: auto;
  transition: background-color 0.3s, color 0.3s;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 18vh;
  left: 10vw;
}

.button:hover {
  background-color: #FFF; 
  color: #FF7F50; 
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}


.bubble-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: 0;
}

.bubble {
  position: absolute;
  background-color: #FF7F50;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  animation: bubbleAnimation 5s infinite;
  opacity: 0;
}

@keyframes bubbleAnimation {
  0% {
    transform: translateY(0) scale(0);
    opacity: 1;
  }
  10% {
    opacity: 1;
  }
  90% {
    opacity: 1;
  }
  100% {
    transform: translateY(-100px) scale(1);
    opacity: 0;
  }
}

@media screen and (max-width: 768px){
  #user, #intro {
  width: 50%;
  padding: 15px;
  margin-bottom: 20px;
  min-width: 60vh;
  border: 1px solid #CCC;
  border-radius: 5px;
  flex-direction: column;
  position: relative;
  top: 18px;
  margin-left: auto;
  margin-right: auto;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
  .button {
  font-family: "Verdana", sans-serif; 
  background-color: #FF7F50;
  color: #FFF;
  padding: 10px 30px;
  border: 5px;
  border-radius: 5px;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center; 
  position: relative;
  margin-left: auto;
  margin-right: auto;
  transition: background-color 0.3s, color 0.3s;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 24vh;
  left: 15vw;
}
  
}
@media only screen and (max-width: 600px) {
  h1 {
  color: #FF7F50;
  font-size: 45px;
  margin-bottom: 20px;
  font-family: "Verdana", sans-serif; 
  letter-spacing: 2px; 
  text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.1); 
  position: absolute;
  left: 50%;
  top: 30%;
  transform: translate(-50%, -50%);
}

#user, #intro {
  width: 50%;
  padding: 15px;
  margin-bottom: 20px;
  min-width: 60vh;
  border: 1px solid #CCC;
  border-radius: 5px;
  flex-direction: column;
  position: relative;
  top: 18px;
  margin-left: auto;
  margin-right: auto;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
  .button {
  font-family: "Verdana", sans-serif; 
  background-color: #FF7F50;
  color: #FFF;
  padding: 10px 30px;
  border: 5px;
  border-radius: 5px;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center; 
  position: relative;
  margin-left: auto;
  margin-right: auto;
  transition: background-color 0.3s, color 0.3s;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 24vh;
  left: 21vw;
}

  .container {
    padding: 10px;
  }
  
  input[type="text"]{
    font-size: 14px;
  }
  
  button[type="submit"] {
    padding: 8px 16px;
  }
}
</style>
