import React from 'react';
import { useQuery, gql } from '@apollo/client';

const GET_WAREHOUSES = gql`
    {warehouses{ids}}
`;

export function GetWarehouses() {
  const { loading, data } = useQuery(
    GET_WAREHOUSES
  );
  return (
    <>
    <div>
      {loading ? (
        <p>Loading ...</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>id</th>
            </tr>
          </thead>
          <tbody>
            {data}
          </tbody>
        </table>
      )}
    </div>
    
    </>
  );
}