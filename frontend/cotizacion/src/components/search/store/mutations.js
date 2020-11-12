
export const set_result = (state, payload) => {
    state.result = payload;
    state.history_search.push(payload);
}

export const set_status = (state, payload) => {
    state.status = payload;
}
