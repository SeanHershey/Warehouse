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
    <div>
        <ul>
            <li>1
                <table>
                    <tr>
                        <th>1</th>
                        <th>2</th>
                        <th>3</th>
                        <th>4</th>
                    </tr>
                    <tr>
                        <td>5</td>
                        <td>6</td>
                        <th>7</th>
                        <th>8</th>
                    </tr>
                    <tr>
                        <td>9</td>
                        <td>10</td>
                        <td>11</td>
                        <td>12</td>
                    </tr>
                </table>
            </li>
            <li>2
                <table>
                    <tr>
                        <th>1</th>
                        <th>2</th>
                        <th>3</th>
                        <th>4</th>
                    </tr>
                    <tr>
                        <td>5</td>
                        <td>6</td>
                        <th>7</th>
                        <th>8</th>
                    </tr>
                    <tr>
                        <td>9</td>
                        <td>10</td>
                        <td>11</td>
                        <td>12</td>
                    </tr>
                </table>
            </li>
            <li>3
                <table>
                    <tr>
                        <th>1</th>
                        <th>2</th>
                        <th>3</th>
                        <th>4</th>
                    </tr>
                    <tr>
                        <td>5</td>
                        <td>6</td>
                        <th>7</th>
                        <th>8</th>
                    </tr>
                    <tr>
                        <td>9</td>
                        <td>10</td>
                        <td>11</td>
                        <td>12</td>
                    </tr>
                </table>
            </li>
        </ul>
    </div>
    </>
  );
}