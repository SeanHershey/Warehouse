import { gql, useLazyQuery } from '@apollo/client';


const RESET = gql`
    {reset {message}}
`;

const Reset = () => {
    const [reset] = useLazyQuery(RESET);

    return (
        <form id="reset">
            <input type="submit"
                value="Reset"
                onClick={(e) => {
                        e.preventDefault();
                        reset();
                        setTimeout(location.reload.bind(location), 200);}}/>
        </form>
    );
};

export default Reset;