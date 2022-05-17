import styled from 'styled-components';
import Rating from '@mui/material/Rating';
import PropTypes from 'prop-types';

const StarContainer = styled.div`
  StarBorderIcon {
    margin: 20px 10px 20px 0;
    opacity: 0.1;
    cursor: pointer;
    font-size: 50px;
  }

  .yellowStar {
    color: orange;
    opacity: 1;
  }
`;

function RatingForm({ rating, setRating }) {
  return (
    <StarContainer>
      <Rating
        name="simple-controlled"
        value={rating}
        onChange={(event, newValue) => {
          setRating(newValue);
        }}
      />
    </StarContainer>
  );
}

RatingForm.propTypes = {
  rating: PropTypes.number,
  setRating: PropTypes.func.isRequired,
};

RatingForm.defaultProps = {
  rating: 0,
};

export default RatingForm;