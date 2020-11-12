import * as actions from './actions';
import * as mutations from './mutations';
import * as getters from './getters';

export const search = {
    state: {
        history_search: [],
        result: {},
        status: false
    },
    actions,
    mutations,
    getters 
}