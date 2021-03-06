import styled, { css } from 'styled-components';
import PropTypes from 'prop-types';

const Button = styled.button`
  color: #a9a9a9;
  font-size: 1.1rem;
  background: none;
  padding: 0.5rem 1rem;
  border: none;
  cursor: pointer;

  ${props =>
    props.isSelected &&
    css`
      color: #000;
      border-bottom: 1px solid #000;
    `}

  @media screen and (min-width: 1025px) {
    padding: 0.5rem 2rem;
    border-bottom: none;
  }
`;

function MoimCategory({ name, value, isSelected, setSelectedCategory }) {
  return (
    <li>
      <Button
        isSelected={isSelected}
        onClick={() => setSelectedCategory(value)}
      >
        {name}
      </Button>
    </li>
  );
}

MoimCategory.propTypes = {
  name: PropTypes.string.isRequired,
  value: PropTypes.number.isRequired,
  isSelected: PropTypes.bool.isRequired,
  setSelectedCategory: PropTypes.func.isRequired,
};

export default MoimCategory;
