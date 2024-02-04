import axios from 'axios';

const state = {
  plant_diseases: null,
  plant_disease: null
};

const getters = {
  statePlantDiseases: state => state.plant_diseases,
  statePlantDisease: state => state.plant_disease,
};

const actions = {
  async getPlantDiseases({commit}) {
    let {data} = await axios.get('plant_diseases');
    commit('setPlantDiseases', data);
  },
  async viewPlantDisease({commit}, id) {
    let {data} = await axios.get(`plant_disease/${id}`);
    commit('setPlantDisease', data);
  }
};

const mutations = {
  statePlantDiseases(state, plant_diseases){
    state.plant_diseases = plant_diseases;
  },
  statePlantDisease(state, plant_disease){
    state.plant_disease = plant_disease;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};