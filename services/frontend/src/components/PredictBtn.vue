<template>
  <button @click="predict" class="predict-btn">Xem kết quả</button>
</template>

<script>
import axios from "axios";
const sound = require('../assets/result.mp3');


export default {
  name: "PredictBtn",
  props: {
    imageFile: File
  },
  data() {
    return {
      response: null,
    };
  },

  methods: {
    async predict() {
      if (this.imageFile) {
        let audio = new Audio(sound);
audio.play();
        console.log('imageFile: ', this.imageFile);
        const formData = new FormData();
        formData.append("file", this.imageFile);

        try {
          const response = await axios.post(
            "http://localhost:8000/single_file",
            formData,
            {
              headers: {
                "Content-Type": "multipart/form-data",
              },
            }
          );

          this.response = response.data;
          this.$emit("confidence", this.response.class_probability);

          try {
            const plantDiseaseObj = await axios.get(
              "http://localhost:8000/plant_disease/" +
                this.response.predicted_class
            );
            this.$emit("plantDiseaseObj", plantDiseaseObj);
            this.$emit("predictClick", true);
            this.$emit("reset", false);
          } catch (error) {
            console.error(error);
          }
        } catch (error) {
          console.error(error);
        }
      }
    },
  },
};
</script>

<style>
.predict-btn {
  display: block;
  margin-left: auto;
  margin-right: auto;
  background-color: #184226;
  height: 50px;
  width: 200px;
  border-radius: 50px;
  color: white;
  font-family: 'AR One Sans';
  font-size: 24px;
}

.predict-btn:hover {
  background-color: #0d2816;
}
</style>
