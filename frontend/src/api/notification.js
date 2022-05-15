import api from '../utils/apiInstance';

const sendToken = async token => {
  try {
    const { data } = await api.post('/notifications/set/', {
      registration_token: token,
    });

    return data.id;
  } catch (err) {
    throw new Error(err);
  }
};

const deleteToken = async tokenId => {
  try {
    await api.delete(`/notifications/cancel/${tokenId}/`);
  } catch (err) {
    throw new Error(err);
  }
};

const sendNotification = async (targetId, chatType) => {
  if (chatType === 1) {
    try {
      await api.post(`/notifications/personal-chat/${targetId}/`); // pairId
    } catch (err) {
      throw new Error(err);
    }
  }

  if (chatType === 2) {
    try {
      await api.post(`/notifications/moim-chat/${targetId}/`); // moimId
    } catch (err) {
      throw new Error(err);
    }
  }
};

export { sendToken, deleteToken, sendNotification };
