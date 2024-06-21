import { useQuery, gql } from '@apollo/client';


const GET_STATUS = gql`
    {getStatus { 
        message}}
`;

export function GetStatus() {
    const { loading, data } = useQuery(GET_STATUS);
    return (
        <>
        {loading ? (
            <p/>
        ) : ( 
            <p>
                {data.getStatus.message}
            </p>
        )}
        </>
  );
}
