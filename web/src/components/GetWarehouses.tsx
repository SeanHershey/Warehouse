import { useQuery, gql } from '@apollo/client';

const GET_WAREHOUSES = gql`
    {warehouses{results}}
`;

const test_results = [
    {
      "name": "test",
      "zone": 1,
      "warehouse": 3
    },
    {
      "name": "test1",
      "zone": 1,
      "warehouse": 4
    },
    {
      "name": "test2",
      "zone": 1,
      "warehouse": 4
    },
    {
      "name": "testnewzone",
      "zone": 2,
      "warehouse": 3
    },
    {
      "name": "test4",
      "zone": 1,
      "warehouse": 4
    },
    {
      "name": "test5",
      "zone": 1,
      "warehouse": 4
    },
    {
      "name": "test6",
      "zone": 1,
      "warehouse": 4
    },
    {
      "name": "test7",
      "zone": 1,
      "warehouse": 4
    },
    {
      "name": "test8",
      "zone": 1,
      "warehouse": 4
    },
    {
      "name": "test9",
      "zone": 1,
      "warehouse": 4
    },
    {
      "name": "test10",
      "zone": 1,
      "warehouse": 4
    },
    {
      "name": "test12",
      "zone": 2,
      "warehouse": 4
    },
    {
      "name": null,
      "zone": null,
      "warehouse": 8
    },
    {
      "name": null,
      "zone": null,
      "warehouse": 6
    },
    {
      "name": null,
      "zone": null,
      "warehouse": 7
    },
    {
      "name": null,
      "zone": null,
      "warehouse": 5
    }
]

export function GetWarehouses() {
  const { loading, data } = useQuery(
    GET_WAREHOUSES
  );
  console.log(data);
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
            {test_results.map((item:any, i:any) => (
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
