import apiInstance from '../utils/apiInstance';

/* 식당 전체 목록 */
export async function apiGetAllRestau() {
  try {
    const response = await apiInstance.get('/greenmates/restaurant/all/');
    return response.data;
  } catch (error) {
    alert('식당 정보를 불러오는데 실패했습니다');
    return error;
  }
}

/* 식당 검색 결과 */
export async function apiGetSearchRestau(data) {
  try {
    const response = await apiInstance.get(
      `/greenmates/restaurant/search/?word=${data.keyword}`,
    );
    return response.data;
  } catch (error) {
    return null;
  }
}

/* 식당 기본 정보 */
export async function apiGetSummaryRestau(data) {
  try {
    const response = await apiInstance.get(
      `/greenmates/restaurant/${data.restauId}/`,
    );
    return response.data;
  } catch (error) {
    return null;
  }
}

/* 식당 상세 정보 */
export async function apiGetDetailRestau(data) {
  try {
    const response = await apiInstance.get(
      `/greenmates/restaurant/detail/${data.restauId}/`,
    );
    return response.data;
  } catch (error) {
    return null;
  }
}

/* 식당 좋아요 */
export function apiPostLikeRestau(data, res, err) {
  apiInstance
    .post(`/greenmates/restaurant/like/${data.restauId}/`)
    .then(res)
    .catch(err);
}

/* 같이 먹기 모임 검색 */
export function apiGetLetseatMoim(data, res, err) {
  apiInstance
    .get(`/greenmates/mates/search/${data.restauId}/`)
    .then(res)
    .catch(err);
}
