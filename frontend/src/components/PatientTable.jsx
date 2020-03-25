import React from "react";

import {
  useTable,
  useFilters,
  useSortBy,
  usePagination
} from 'react-table';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";


function Table({columns, data}) {
  const {
    getTableProps,
    getTableBodyProps,
    headers,
    prepareRow,
    pageOptions,
    page,
    state: { pageIndex, pageSize },
    gotoPage,
    previousPage,
    nextPage,
    canPreviousPage,
    canNextPage,
    pageCount,
    setPageSize,
  } = useTable({
      columns, data
    },
    useSortBy,
    usePagination);


  return (
    <div>
      <table {...getTableProps()} className="table table-responsive">
        <thead>
        <tr>
            {headers.map(column => (
              <th {...column.getHeaderProps(column.getSortByToggleProps())}>
                <span className="mr-2">
                  {column.render('Header')}
                </span>
                <i className="d-inline">

                {
                  column.isSorted ?
                    (column.isSortedDesc ?
                      <FontAwesomeIcon icon="sort-amount-down" />:
                      <FontAwesomeIcon icon="sort-amount-up" />
                  ) : <FontAwesomeIcon icon="sort"/>
                }
                </i>
              </th>
            ))}
          </tr>
        </thead>
        <tbody {...getTableBodyProps()}>
        {page.map((row, i) => {
          prepareRow(row);
          return (
            <tr {...row.getRowProps()}>
              {row.cells.map(cell => {
                return <td {...cell.getCellProps()}>{cell.render('Cell')}</td>
              })}
            </tr>
          )
        })}
        </tbody>
      </table>

      <div className="row align-items-baseline border-top p-2 justify-content-center">
        <div className="col-6 col-md-3">
          <span className="mr-2">Show</span>
          <select
            value={pageSize}
            onChange={e => {
              setPageSize(Number(e.target.value))
            }}
            className="form-control form-control-sm d-inline"
            style={{ width: '5rem' }}
          >
            {[10, 20, 30, 40, 50].map(pageSize => (
              <option key={pageSize} value={pageSize}>
                {pageSize}
              </option>
            ))}
          </select>
          <span className="mx-2">per page</span>
        </div>

        <div className="col-6 col-md-3 text-center">
          <p className="text-left text-md-right">
            Page{' '}
            <strong>
              {pageIndex + 1} of {pageOptions.length}
            </strong>
          </p>
        </div>

        <div className="col-6 col-md-3">
          <ul className="pagination mt-2">
            <li className="page-item">
              <button className="page-link" onClick={() => gotoPage(0)} disabled={!canPreviousPage}>
                <FontAwesomeIcon icon='angle-double-left' />
              </button>
            </li>
            <li className="page-item">
              <button className="page-link"  onClick={() => previousPage()} disabled={!canPreviousPage}>
                <FontAwesomeIcon icon='chevron-left' />
              </button>
            </li>
            <li className="page-item">
              <button className="page-link" onClick={() => nextPage()} disabled={!canNextPage}>
                <FontAwesomeIcon icon='chevron-right' />
              </button>
            </li>
            <li className="page-item">
              <button className="page-link" onClick={() => gotoPage(pageCount - 1)} disabled={!canNextPage}>
                <FontAwesomeIcon icon="angle-double-right" />
              </button>
            </li>
          </ul>
        </div>

       <div className="col-6 col-md-3 text-right">
          Go to page:{' '}
          <input
            type="number"
            defaultValue={pageIndex + 1}
            onChange={e => {
              const page = e.target.value ? Number(e.target.value) - 1 : 0;
              gotoPage(page)
            }}
            style={{ width: '3rem' }}
            className="form-control form-control-sm d-inline"
          />
        </div>
      </div>
    </div>
  );
}

function PatientTable({ patients }) {
  const columns = React.useMemo(()=> [
      {
        Header: 'ID',
        accessor: 'id'
      }, {
        Header: 'Diagnosed Date',
        accessor: 'diagnosed_date'
      }, {
        Header: 'Age',
        accessor: 'age'
      }, {
        Header: 'Gender',
        accessor: 'gender'
      }, {
        Header: 'City',
        accessor: 'detected_city'
      }, {
        Header: 'State',
        accessor: 'detected_state'
      }, {
        Header: 'Status',
        accessor: 'current_status'
      }],
    []
  );
  const data = React.useMemo(() => (patients), [patients]);

  return <Table columns={columns} data={data} />;
}

export default PatientTable
