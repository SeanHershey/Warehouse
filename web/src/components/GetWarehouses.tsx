import React from 'react';
import { useQuery, gql } from '@apollo/client';
import { BuildTable } from './BuildTable';

const GET_WAREHOUSES = gql`
    {warehouses{results}}
`;

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
            <ul>
                {[{name:"hello"},{name:"there"}].map((line:any) => (
                    <li>{line.name}</li>
                ))}
            </ul>
      )}
    </div>
    
    </>
  );
}
