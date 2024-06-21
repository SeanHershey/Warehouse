import { useQuery, gql } from '@apollo/client';

const GET_SHELVES = gql`
    {getShelves {results}}
`;

export function GetShelves() {
  const { loading, data } = useQuery(GET_SHELVES);
  return (
    <>
    <div>
      {loading ? (
        <p>Loading ...</p>
      ) : (
        <table>
            <thead>
            <tr key="legend">
                <th>Warehouse</th>
                <th>Name</th>
                <th>Zone</th>
            </tr>
            </thead>
            <tbody>
            {data.getShelves.results.map((item:any, i:any) => (
                <tr key={i}>
                    <td>{item.warehouse}</td>
                    <td>{item.name}</td>
                    <td>{item.zone}</td>
                </tr>
            ))}
            </tbody>
        </table>
      )}
    </div>
    
    </>
  );
}
